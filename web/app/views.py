#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: LonJE

from app import app, es
from flask import (render_template, redirect, url_for,
                   request, session)
from flask_paginate import Pagination

from app.util import search_body


@app.route('/')
def home():
    form = 0
    return render_template('index.html', form=form)


@app.route('/search', methods=['POST'])
def search():
    form = request.form
    query = form['query']
    return redirect(url_for('search_results', query=query))


@app.route('/search-results/<path:query>')
def search_results(query):
    page = int(request.args.get('page', 1))
    per_page = app.config['PER_PAGE']

    body = search_body(query)
    response = es.search(
            index=app.config['ES_INDEX'],
            # doc_type='',
            from_=(page-1)*per_page,
            size=per_page,
            body=body
            )
    search_results = response['hits']['hits']
    results_count = response['hits']['total']

    pagination = Pagination(
            css_framework=app.config['CSS_FRAMEWORK'],
            page=page,
            total=results_count,
            per_page=per_page)
    return render_template('search_results.html',
            query=query,
            search_results=search_results,
            pagination=pagination,
            count=results_count)
