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

from flask import Flask, render_template
from flaskext.uploads import configure_uploads

from life.config import Config, DevConfig, ProConfig
from life.extensions import db, photos, login_manager

from life import views
#from life.views import login_manager
from life.models import Anonymous
from life.views import frontend, user, account

__all__ = ['create_app']

## 默认应用程序名称, 与二级目录名称一致
DEFAULT_APP_NAME = "life"

## 程序模块
## DEFAULT_MODULES = (
##     (views.frontend, ""),
##     (views.user, "/user"),
##     (views.account, "/account"),
##     )

DEFAULT_BLUEPRINTS = (
    frontend,
    user,
    account,
    )

def create_app(config=None, app_name=None, blueprints=None):
    """创建应用配置"""
    
    if app_name is None:
        app_name = DEFAULT_APP_NAME

    ## if modules is None:
    ##     modules = DEFAULT_MODULES

    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS
        
    app = Flask(app_name)

    configure_app(app, config)
    ## configure_modules(app, modules)
    configure_blueprints(app, blueprints)
    configure_extensions(app)
    configure_login(app)

    configure_errorhandler(app)
    configure_uploads(app, photos)  ## 图片上传配置

    return app

def configure_app(app, config):
    """调用运行环境配置"""
    
    app.config.from_object(DevConfig())

    if config is not None:
        app.config.from_object(config)

    app.config.from_envvar("APP_CONFIG", silent=True)

## def configure_modules(app, modules):
##     """配置网站相关模块"""
    
##     for module, url_prefix in modules:
##         app.register_module(module, url_prefix=url_prefix)

def configure_blueprints(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
        
def configure_extensions(app):
    """配置各类扩展"""
    
    db.init_app(app)

def configure_login(app):
    login_manager.anonymouse = Anonymous
    login_manager.login_view = 'account.login'
    #login_manager.login_message = u"请你登录"
    
    login_manager.setup_app(app)
    
def configure_errorhandler(app):
    """各种错误"""

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('error/page_404.html'), 404
