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

from flask import Blueprint, Module, render_template, request, url_for, redirect, flash, abort, g
from flaskext.uploads import UploadNotAllowed
from flaskext.login import login_required, current_user  ## 用户登录认证

from life.extensions import db, photos
from life.models import Spot, Concern, User
from life.forms import SpotForm

## 用户后台管理视图
user = Blueprint('user', __name__)

@user.route("/")
@user.route("/index")
@login_required
def index():
    return render_template("user/index.html")

def get_user_id(username):
    """获得用户ID"""
    user = User.query.filter_by(username=username).first()

    if user is None:
        #print 'not found!'
        abort(404)
        
    return user.id

@user.route("/addspot", methods=['GET', 'POST'])
@login_required
def addspot():
    form = SpotForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        spot_name = form.spot_name.data
        logo = request.files.get("spot_logo")
        spot_loc = form.spot_loc.data
        better_season = form.better_season.data
        tickets = form.tickets.data
        content = form.content.data

        try:
            spot_logo = photos.save(logo)  ## 保存图片
        except UploadNotAllowed:
            flash("The upload was not allowed")

        spot = Spot(spot_name=spot_name,
                    spot_loc=spot_loc,
                    spot_logo=spot_logo,
                    better_season=better_season,
                    tickets=tickets,
                    content=content)
        try:
            spot._store_to_db()
            flash(u"数据保存成功!")
        except:
            flash(u"保存失败")

        return redirect(url_for("user.index"))
            
    return render_template("user/addspot.html", form=form)

@user.route("/spotmanager")
@login_required
def spot_manager():
    spots = Spot.query.order_by('-id')

    return render_template("user/spotmn.html", spots=spots)

@user.route("/spot/<int:id>/del")
@login_required
def spot_del(id):
    spot = Spot.query.filter_by(id=id).first()

    if spot:
        spot._delete_from_db()
        
    return redirect(url_for('user.spot_manager'))

@user.route("/spot/<int:id>/edit", methods=['GET', 'POST'])
@login_required
def spot_edit(id):
    spot = Spot.query.filter_by(id=id).first()

    if not spot:
        abort(404)

    form = SpotForm(spot_name=spot.spot_name,
                    spot_loc=spot.spot_loc,
                    better_season=spot.better_season,
                    tickets=spot.tickets,
                    content=spot.content)
    if request.method == 'POST' and form.validate_on_submit():
        logo = request.files.get("spot_logo")

        try:
            spot_logo = photos.save(logo)
        except UploadNotAllowed:
            flash("The upload was not allowed")
            
        Spot.query.filter_by(id=id).update({
            Spot.spot_name: request.form['spot_name'],
            Spot.spot_logo: spot_logo,
            Spot.spot_loc: request.form['spot_loc'],
            Spot.better_season: request.form['better_season'],
            Spot.tickets: request.form['tickets'],
            Spot.content: request.form['content']})
        db.session.commit()

        return redirect(url_for('user.spot_manager'))

    return render_template('user/spotedit.html', form=form)

@user.route("/<int:id>/beento")
def beento(id):
    if not current_user.is_authenticated():
        return redirect(url_for("accounts.login"))
    print current_user.name
    user_id = get_user_id(current_user.name)

    con = Concern(user_id=user_id,
                  spot_id = id,
                  beento = True)
    try:
        con._store_to_db()
        flash(u"你又多了一个去过的地主！")
    except:
        pass

    return redirect(url_for('frontend.spot_one', id=id))

@user.route("/<int:id>/wantto")
def wantto(id):

    if not current_user.is_authenticated():
        return redirect(url_for("accounts.login"))
    
    user_id = get_user_id(current_user.name)

    con = Concern(user_id=user_id,
                  spot_id=id,
                  wantto=True)

    try:
        con._store_to_db()
        flash(u"又一个你想去的地方")
    except:
        pass

    return redirect(url_for('frontend.spot_one', id=id))

@user.route("/wb")
def manager_been_want():
    
    usernmae = current_user.name
    wb = Concern.query.filter_by(username=username).all()

    spots = Spot.query(id=wb.spot_id).all()

    return render_template('user/wb.html', spots=spots)
    
