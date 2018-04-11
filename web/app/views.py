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

    body = search_body(query)
    response = es.search(
            index=app.config['ES_INDEX'],
            # doc_type='',
            from_=(page-1)*20,
            size=20,
            body=body
            )
    search_results = response['hits']['hits']
    results_count = response['hits']['total']

    pagination = Pagination(
            page=page,
            total=results_count,
            per_page=20)
    return render_template('search_results.html',
            query=query,
            search_results=search_results,
            pagination=pagination,
            count=results_count)
