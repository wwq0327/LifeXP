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

__all__ = ['db']

db = SQLAlchemy()
