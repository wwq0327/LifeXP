#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    accounts.py
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-09-25
    :author: wwq0327 <wwq0327@gmail.com>
    :license: GPLv3
"""

from flaskext.wtf import Form, TextField, PasswordField, BooleanField,\
     SubmitField, required

class LoginForm(Form):
    username = TextField(u"用户名", validators=[required()])
    password = PasswordField(u"密码", validators=[required()])
    submit = SubmitField(u"登录")
