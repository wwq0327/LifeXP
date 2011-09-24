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

## 用户后台管理视图
bc = Module(__name__)

@bc.route("/")
@bc.route("/index")
def index():
    return render_template("user/index.html")

@bc.route("/addspot")
def addspot():
    return render_template("user/addspot.html")
