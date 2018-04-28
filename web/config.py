#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: LonJE

SECRET_KEY = 'lyc_search'

WTF_CSRF_ENABLED = True
TEMPLATES_AUTO_RELOAD = True

ELASTICSEARCH_HOST = "127.0.0.1:9200"
ES_INDEX = 'lyc_ik'

CSS_FRAMEWORK = 'bootstrap3'

PER_PAGE=20

# For local settings >>>
try:
    from local_settings import *
except:
    pass
