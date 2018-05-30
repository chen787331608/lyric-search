#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: LonJE

import click
from gevent.pywsgi import WSGIServer
from app import app

@click.command()
@click.option('--port', '-p', default=5000, help='listening port')
def run(port):
    # app.run(debug=True, port=port)
    http_server = WSGIServer(('127.0.0.1', port), app)
    http_server.serve_forever()

if __name__ == '__main__':
    run()
