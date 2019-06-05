#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : __init__.py.py
 @Author: Junyue
 @Date  : 2019/5/18
 @Desc  :
"""
from flask import Flask
from flask.json import JSONEncoder
from flask_login import LoginManager
# from flask_cache import Cache

from app.model import db

login_manager = LoginManager()
# cache = Cache(config={'CACHE_TYPE': 'simple'})

# class JSONEncoder(_JSONEncoder):
#     def default(self, o):
#         if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
#             return dict(o)
#
#
# class Flask(_Flask):
#     json_encoder = JSONEncoder

def register_blueprint(app):
    from .view import web
    app.register_blueprint(web)

def create_app():

    app = Flask(__name__)

    # app.wsgi_app = CasbinMiddleware(app.wsgi_app)

    app.config.from_object('conf.setting')
    app.config.from_object('conf.secret')

    register_blueprint(app)

    # 注册SQLAlchemy
    db.init_app(app)

    # 注册login模块
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    # login_manager.login_message = '请先登录或注册'

    # 注册flask-cache模块
    # cache.init_app(app)

    return app

