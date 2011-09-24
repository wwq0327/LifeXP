#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    SpotForm.py
    ~~~~~~~~~~~~~~~~~~~~

    景点添加表单
    
    :date: 2011-09-24
    :author: wwq0327 <wwq0327@gmail.com>
    :license: GPLv3
"""

from flaskext.wtf import Form, TextField, TextAreaField, SubmitField, required, FloatField

class SpotForm(Form):

    spot_name = TextField(u"景点名称", validators=[required(message=u"景点名称")])
    spot_loc = TextField(u"景点位置")
    better_season = TextField(u"理想出行季节")
    tickets = FloatField(u"票价")
    content = TextAreaField(u"景点介绍")
    spot_logo = TextField(u"图片")
    submit = SubmitField(u"发布景点")
