#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: LonJE

from flask import Flask
from flask_elasticsearch import FlaskElasticsearch


app = Flask(__name__)
app.config.from_object('config')

es = FlaskElasticsearch(app, timeout=1000)

__import__('app.views')
