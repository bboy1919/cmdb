#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : deploy.py
 @Author: Junyue
 @Date  : 2019/5/31
 @Desc  :
"""
from flask import render_template, session

from app.view import web

@web.route("/project/deploy")
def deploy_index():
    return render_template("deploy.html" ,info=session)