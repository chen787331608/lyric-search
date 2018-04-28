# 歌词检索Demo
#### [测试Demo](http://118.24.45.23:8085/)

### 一、说明
- 爬虫采用python的scrapy + BeautifulSoup解析
- ElasticSearch请在ES官网下载，采用客户端py-elasticsearch
- 歌词网站来源：[酷我](http://www.kuwo.cn/artist/index)
- web使用flask, Python Web  （[进行中](https://github.com/chen787331608/lyric-search)）

### 二、歌词网站分析
> a) 歌手获取分析
从js中找到分页请求的url,
var b = host + "/artist/indexAjax?category=" + index + "&prefix=" + $("#artistContent").attr("data-letter") + "&pn=" + pn;
如http://www.kuwo.cn/artist/indexAjax?category=0&prefix=&pn=5
构造url   参数pn为当前页码 范围 （pn:0-6947）

> b)歌词分页获取分析
如：http://www.kuwo.cn//artist/contentMusicsAjax?artistId=2&pn=1&rn=100
其中artistId为歌手id，pn为分页参数
接下来循环遍历即可

> c)歌词获取分析
每首歌歌词的详情页  http://www.kuwo.cn/yinyue/6468891
注意：此处有时因为无版权，无法显示歌词，需要增加异常处理
### 三、python爬虫解析代码
##### 使用 scrapy 管理爬虫
启动方法 : 进入目录 `cd kuwolyc`  执行`scrapy crawl lyc`

### 四、ES-docker部署，
Docker页面：https://hub.docker.com/_/elasticsearch/
##### docker部署方法
中文参考  http://kael-aiur.com/docker/%E5%9C%A8docker%E4%B8%8A%E8%BF%90%E8%A1%8Celasticsearch.html

##### 加入 ik-analysis
> https://github.com/medcl/elasticsearch-analysis-ik  *IK Analysis for Elasticsearch*
##### ES mappings
```json
{
  "properties": {
    "album": {
      "type": "text",
      "fields": {
        "keyword": {
          "type": "keyword",
          "ignore_above": 256
        }
      }
    },
    "href": {
      "type": "text",
      "fields": {
        "keyword": {
          "type": "keyword",
          "ignore_above": 256
        }
      }
    },
    "lyric": {
      "type": "text",
      "analyzer": "ik_smart"
    },
    "name": {
      "type": "text",
      "analyzer": "ik_max_word"
    },
    "singer": {
      "type": "text",
      "fields": {
        "keyword": {
          "type": "keyword",
          "ignore_above": 256
        }
      }
    }
  }
}
```
导入脚本 [json2es.py](json2es.py)

### 五、构建web （python3）
 
```bash
# 进入web目录
cd web
# 配置flask环境
pip install -r requirements.txt
# 运行web app 
python run.py --port 8085
```
