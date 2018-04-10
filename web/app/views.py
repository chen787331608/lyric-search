#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: LonJE

from app import app, es
from flask import render_template, redirect, url_for


@app.route('/')
def home():
    form = 0
    return render_template('index.html', form=form)


@app.route('/search')
def search():
    return render_template('index.html', form=form)
