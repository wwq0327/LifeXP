#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    frontend.py
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-09-24
    :author: wwq0327 <wwq0327@gmail.com>
    :license: GPLv3
"""

from flask import Module, render_template

from life.models import Spot

frontend = Module(__name__)

@frontend.route("/")
def index():
    spots = Spot.query.order_by('-id')
    
    return render_template("frontend.html", spots=spots)
