#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    accounts.py
    ~~~~~~~~~~~~~~~~~~~~
    
    :date: 2011-09-25
    :author: wwq0327 <wwq0327@gmail.com>
    :license: GPLv3
"""

from werkzeug import generate_password_hash, check_password_hash
from flaskext.login import AnonymousUser, UserMixin

from life.extensions import db

class Anonymous(AnonymousUser):
    name = u"Guest"

class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    is_active = db.Column(db.Boolean())

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return self.username

    def store_to_db(self):
        db.session.add(self)
        db.session.commit()

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class LoginUser(UserMixin):
    def __init__(self, id, name, active=True):
        self.id = id
        self.name = name
        self.active = active

    def is_active(self):
        return self.active

class Beento(db.Model):
    __tablename__ = 'beento'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    spot_id = db.Column(db.Integer)
    beento = db.Column(db.Boolean())
    ##wantto = db.Column(db.Boolean())

    def __init__(self, *args, **kwargs):
        super(Concern, self).__init__(*args, **kwargs)

    def _repr__(self):
        return "<Concern %s>" % self.user_id

    def _store_to_db(self):
        db.session.add(self)
        db.session.commit()

class Wantto(db.Model):
    __tablename__ = 'wantto'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    spot_id = db.Column(db.Integer)
    ##beento = db.Column(db.Boolean())
    wantto = db.Column(db.Boolean())

    def __init__(self, *args, **kwargs):
        super(Concern, self).__init__(*args, **kwargs)

    def _repr__(self):
        return "<Concern %s>" % self.user_id

    def _store_to_db(self):
        db.session.add(self)
        db.session.commit()
