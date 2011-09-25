#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    accounts.py
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-09-25
    :author: wwq0327 <wwq0327@gmail.com>
    :license: GPLv3
"""

from flask import Blueprint, Module, request, render_template, redirect, url_for, flash

from flaskext.login import (current_user, login_required, login_user,
                          logout_user, UserMixin, AnonymousUser, confirm_login,
                          fresh_login_required)

from life.models import Anonymous, User, LoginUser
from life.forms import LoginForm
from life.views import user
from life.extensions import login_manager

#account = Module(__name__)
accounts = Blueprint('accounts', __name__)

## login_manager = LoginManager()
## login_manager.anonymous_user = Anonymous
## login_manager.login_view = 'accounts.login'
## login_manager.login_message = u'你需要登录后才能进行下一步操作'

@login_manager.user_loader
def load_user(id):
    try:
        return LoginUser(int(id), User.query.get(id).username)
    except:
        return None

@accounts.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = 1

        user = User.query.filter_by(username=username).first()
        if not len(form.errors):
            if user and user.check_password(password):
                loginuser = LoginUser(user.id, user.username)
                if login_user(loginuser, remember=remember):
                    #flash(u"登录成功")
                    #return redirect(request.args.get('next') or "/user/index")
                    return redirect(request.args.get('next') or url_for("user.index"))
                ## else:
                ##     flash(u"登录失败")
            else:
                flash(u"用户名不存在，或与密码不匹配")

    return render_template("user/login.html", form=form)

@accounts.route('/logout')
@login_required
def logout():
    logout_user()
    flash(u"你已退出后台管理界面，如需进行设置请登录")
    return redirect(url_for('frontend.index'))
