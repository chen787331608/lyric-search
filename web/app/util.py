#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: LonJE

import re

fields = ["singer", "name", "lyric"]

def highlight_term():
    return {
            "highlight":{
                "pre_tags": ["<b>"],
                "post_tags": ["</b>"],
                "fields": {
                    "name": {"number_of_fragments": 0},
                    "lyric": {"number_of_fragments": 0}
                    }
                }
            }


def aggs_term():
    return {}


def common_body(query):
    body = {
            "query": {
                "bool": {
                    "should": [
                        {
                            "multi_match": {
                                "query": query,
                                "type": "phrase",
                                "fields": fields
                                }
                            }
                        ]
                    }
                }
            }
    return body


def simple_body(query):
    body = { 
            "query": {
                "bool": {
                    "should": [
                        {   
                            "simple_query_string": {
                                "query": query,
                                "default_operator": "and",
                                "fields": fields
                                }   
                            }   
                        ]   
                    }   
                }   
            }   
    return body


def search_body(query):
    if re.match(r'\".+\"|-\S', query):
        query = re.sub('\s*([\+\-\|])\s*', r'\1', query)
        body = simple_body(query)
    else:
        body = common_body(query)
    body.update(highlight_term())
    body.update(aggs_term())
    return body
