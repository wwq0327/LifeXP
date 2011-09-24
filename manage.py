#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    manage.py
    ~~~~~~~~~~~~~~~~~~~~

    应用主程序，执行后即可启动网站
    
    :date: 2011-09-24
    :author: wwq0327 <wwq0327@gmail.com>
    :license: GPLv3
"""

from flask import current_app

from flaskext.script import Manager, Server

from life import create_app
from life.extensions import db
from life.models import Spot

manager = Manager(create_app)

server = Server(host='127.0.0.1', port=8888)
manager.add_command("runserver", server)


@manager.command
def createall():
    db.create_all()

@manager.command
def dropall():
    db.drop_all()

@manager.shell
def make_shell_context():
    return dict(app=create_app,
                db=db,
                Spot=Spot)

if __name__ == '__main__':
    manager.run()
