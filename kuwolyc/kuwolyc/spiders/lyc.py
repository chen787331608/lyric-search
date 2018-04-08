# -*- coding: utf-8 -*-
import json
import scrapy
import logging
from bs4 import BeautifulSoup


logger = logging.getLogger(__name__)


class LycSpider(scrapy.Spider):
    name = 'lyc'
    allowed_domains = ['www.kuwo.cn']
    # start_urls = ['http:///']
    website_possible_httpstatus_list = [404, 302, 200]
    handle_httpstatus_list = [302]
    
    bast_url = 'http://www.kuwo.cn'
    data_page = 0

    def start_requests(self):
        url = 'http://www.kuwo.cn/artist/indexAjax?category=0&prefix=&pn='
        for page in range(6931):
            yield scrapy.FormRequest(url + format(page),
                                     callback=self.get_sger_list)

    def get_sger_list(self, response):
        xml = response.body
        soup = BeautifulSoup(xml, 'lxml')
        t = soup.find_all('a', class_="artistLeft fl")
        sger_list = [self.bast_url+i['href'] for i in t]
        for sger_url in sger_list:
            yield scrapy.FormRequest(sger_url, callback=self.get_music_list)

    def get_music_list(self, response):
        xml = response.body
        soup = BeautifulSoup(xml, 'lxml')
        artist_id = soup.find('div', class_='artistTop')
        try:
            artist_id = artist_id['data-artistid']
        except:
            logger.info(u"artist_id is None ! Please Check")
        self.data_page = 1
        data_pn = 0
        while self.data_page > data_pn:
            url = self.bast_url + \
                  '/artist/contentMusicsAjax?artistId={}&pn={}&rn=100'.format(artist_id, data_pn)
            yield scrapy.FormRequest(url, callback=self.get_lyc)
            data_pn += 1

    def get_lyc(self, response):
        xml = response.body
        soup = BeautifulSoup(xml, 'lxml')
        data_page = soup.find('ul', class_='listMusic')['data-page']
        self.data_page = int(data_page)
        t = soup.find_all('div', class_="name")
        music_list_url = [self.bast_url+i.a['href'] for i in t]
        for music_url in music_list_url:
            yield scrapy.FormRequest(music_url, callback=self.save_items)

    def save_items(self, response):
        xml = response.body
        soup = BeautifulSoup(xml, 'lxml')
        music_soup = soup.find('div', id='musiclrc')
        if not music_soup:
            logger.info(u"无法获取歌曲内容 ! Please Check\t" + response.url)
            return None
        song_name = music_soup.find('p', id='lrcName').text
        singer = music_soup.find('p', class_='artist').span.text
        album = music_soup.find('p', class_='album').span.text
        llrcId = music_soup.find('div', id='llrcId')
        if llrcId:
            llyc =llrcId.find_all('p')
            lyc_list = [i.text for i in llyc]
        else:
            logger.info(u"无歌词 !  " + response.url)
            lyc_list = [u'无歌词']
        href = response.url
        _id = href[href.rfind('/')+1:]
        # with open('../lyc_data/{}.txt'.format(song_name), 'w') as f:
        #     f.write('\n'.join(lyc_list))
        with open('../lyc_data/{}_{}.json'.format(song_name, _id), 'w') as f:
            json_dict = {
                    'name': song_name,
                    'singer': singer,
                    'album': album,
                    'href': href,
                    'lyric': lyc_list
                         }
            f.write(json.dumps(json_dict, indent=4))

