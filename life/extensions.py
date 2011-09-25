#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    extensions.py
    ~~~~~~~~~~~~~~~~~~~~

    扩展集成中心
    
    :date: 2011-09-24
    :author: wwq0327 <wwq0327@gmail.com>
    :license: GPLv3
"""

from flaskext.sqlalchemy import SQLAlchemy
from flaskext.uploads import UploadSet, IMAGES
from flaskext.login import LoginManager

__all__ = ['db', 'photos']

db = SQLAlchemy()  ## 数据库
photos = UploadSet('photos', IMAGES) ## 图片上传扩展
login_manager = LoginManager()
