#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: LonJE

def highlight_term():
    return {}


def aggs_term():
    return {}


def common_body(query):
    body = {
            "query":{
                "match_all": {}
                }
            }
    return body

def search_body(query):
    body = common_body(query)
    body.update(highlight_term())
    body.update(aggs_term())
    return body
