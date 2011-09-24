#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    spot.py
    ~~~~~~~~~~~~~~~~~~~~

    景点数据模块
    
    :date: 2011-09-24
    :author: wwq0327 <wwq0327@gmail.com>
    :license: GPLv3
"""

from datetime import datetime

from life.extensions import db, photos

class Spot(db.Model):
    """景点数据模型"""

    __tablename__ = 'spot'

    id = db.Column(db.Integer, primary_key=True)
    spot_name = db.Column(db.String(120), nullable=False)
    spot_loc = db.Column(db.String(60))
    better_season = db.Column(db.String(30))
    tickets = db.Column(db.Float)
    content = db.Column(db.Text)
    spot_logo = db.Column(db.String(200))
    posted_on = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, *args, **kwargs):
        super(Spot, self).__init__(*args, **kwargs)

    def __repr__(self):
        return "<Spot %s>" % self.spot_name

    def _store_to_db(self):
        """将数据添加到数据库中"""
        
        db.session.add(self)
        db.session.commit()

    def _delete_from_db(self):
        """从数据库中删除数据条目"""
        
        db.session.delete(self)
        db.session.commit()

    @property
    def imgsrc(self):
        if not self.spot_logo:
            return None
        
        return photos.url(self.spot_logo)
