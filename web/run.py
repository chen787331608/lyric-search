#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: LonJE

import click
from app import app

@click.command()
@click.option('--port', '-p', default=5000, help='listening port')
def run(port):
    app.run(debug=True, port=port)

if __name__ == '__main__':
    run()
