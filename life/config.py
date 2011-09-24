#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    config.py
    ~~~~~~~~~~~~~~~~~~~~

    程序配置
    
    :date: 2011-09-24
    :author: wwq0327 <wwq0327@gmail.com>
    :license: GPLv3
"""

import os

_HERE = os.path.dirname(__file__)
_DB_SQLITE_PATH = os.path.join(_HERE, 'lifexp.sqlite')

_DBUSER = "root"  # 数据库用户名
_DBPASS = "123"  # 数据库用户名密码
_DBHOST = "localhost"  # 服务器
_DBNAME = "lifexp"  # 数据库名称

PER_PAGE = 5  # 每页显示文章数
MN_PER_PAGE = 10 # 后台管理中每页文章列表数

#_BLOG_NAME = "Life XP" # Blog名称

class Config(object):
    SECRET_KEY = 'B\xa2\xc3ru\xcd\xac\x039\x836\x93S\x0f2_\x9b\x9d>S\xb91\xb2\xfa'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % _DB_SQLITE_PATH
    BABEL_DEFAULT_TIMEZONE = 'Asia/Chongqing'


class ProConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s/%s' % (_DBUSER, _DBPASS, _DBHOST, _DBNAME)

class DevConfig(Config):
    DEBUG = True

class TestConfig(Config):
    TESTING = True
