#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    user.py
    ~~~~~~~~~~~~~~~~~~~~

    简单的后台简单功能
    
    :date: 2011-09-24
    :author: wwq0327 <wwq0327@gmail.com>
    :license: GPLv3
"""

## :TODO: 用户管理功能

from flask import Module, render_template, request, url_for, redirect, flash, abort

from life.extensions import db
from life.models import Spot
from life.forms import SpotForm

## 用户后台管理视图
bc = Module(__name__)

@bc.route("/")
@bc.route("/index")
def index():
    return render_template("user/index.html")

@bc.route("/addspot", methods=['GET', 'POST'])
def addspot():
    form = SpotForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        spot_name = form.spot_name.data
        spot_loc = form.spot_loc.data
        better_season = form.better_season.data
        tickets = form.tickets.data
        content = form.content.data

        spot = Spot(spot_name=spot_name,
                    spot_loc=spot_loc,
                    better_season=better_season,
                    tickets=tickets,
                    content=content)
        try:
            spot._store_to_db()
            flash(u"数据保存成功!")
        except:
            flash(u"保存失败")

        return redirect(url_for("index"))
            
    return render_template("user/addspot.html", form=form)
