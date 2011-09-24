#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    application.py
    ~~~~~~~~~~~~~~~~~~~~

    应用程序配置程序
    
    :date: 2011-09-24
    :author: wwq0327 <wwq0327@gmail.com>
    :license: GPLv3
"""

from flask import Flask

from life.config import Config, DevConfig, ProConfig
from life.extensions import db

from life import views

__all__ = ['create_app']

## 默认应用程序名称, 与二级目录名称一致
DEFAULT_APP_NAME = "life"

## 程序模块
DEFAULT_MODULES = (
    (views.frontend, ""),
    )

def create_app(config=None, app_name=None, modules=None):
    """创建应用配置"""
    
    if app_name is None:
        app_name = DEFAULT_APP_NAME

    if modules is None:
        modules = DEFAULT_MODULES
        
    app = Flask(app_name)

    configure_app(app, config)
    configure_extensions(app)
    configure_modules(app, modules)

    return app

def configure_app(app, config):
    """调用运行环境配置"""
    
    app.config.from_object(DevConfig())

    if config is not None:
        app.config.from_object(config)

    app.config.from_envvar("APP_CONFIG", silent=True)

def configure_modules(app, modules):
    """配置网站相关模块"""
    
    for module, url_prefix in modules:
        app.register_module(module, url_prefix=url_prefix)

def configure_extensions(app):
    """配置各类扩展"""
    
    db.init_app(app)