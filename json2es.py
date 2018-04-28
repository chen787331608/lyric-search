#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: LonJE

import os
import json
import gc
import logging
import uuid
from time import time, sleep
from elasticsearch import helpers
from elasticsearch import Elasticsearch

from logging.handlers import RotatingFileHandler

file_handler = RotatingFileHandler(
                        'log/parse.log', 'a', 1 * 1024 * 1024, 10) 
file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s: %(lineno)d]')
                ) 
logger = logging.getLogger('json2es')
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

es = Elasticsearch(timeout=100)
data_path = 'lyc_data/'


def es_bulk(actions):
    logger.debug('Adding to ES ...')
    # sleep(3)
    helpers.bulk(es, actions)
    logger.debug('Onece index accomplish')


if __name__ == '__main__':
    count = 0
    list_count = 0
    actions = []
    for root, dirs, files in os.walk(data_path):
        for filename in files:
            if filename.endswith('.json') and not filename.startswith('.'):
                count += 1
                org_file_path = root + '/' + filename
                with open(org_file_path) as f:
                    lyc_file = f.read()
                lyc_dic = json.loads(lyc_file)
                # print(lyc_dic['name'])
                action = {
                            "_index": "lyc_ik",
                            "_type": "sample",
                            "_id": uuid.uuid5(uuid.NAMESPACE_URL, filename),
                            "_source": lyc_dic
                         }
                actions.append(action)
                list_count += 1
                if list_count == 500:
                    es_bulk(actions)
                    list_count = 0
                    del actions[:]
                    gc.collect()
                    logger.info('current Count is {}'.format(count))
    if actions:
        es_bulk(actions)
    logger.info("Finish bulk index.")
