#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    frontend.py
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-09-24
    :author: wwq0327 <wwq0327@gmail.com>
    :license: GPLv3
"""

from flask import Blueprint, Module, render_template

from life.models import Spot, Beento, Wantto

#frontend = Module(__name__)
frontend  = Blueprint('frontend', __name__)

@frontend.route("/")
def index():
    spots = Spot.query.order_by('-id')
    
    return render_template("frontend.html", spots=spots)

@frontend.route('/spot/<int:id>')
def spot_one(id):
    spot = Spot.query.filter_by(id=id).first()

    return render_template('spot.html', spot=spot)
        
@frontend.route('/help')
def help():
    return render_template('help.html')
