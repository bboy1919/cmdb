#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : testing.py
 @Author: Junyue
 @Date  : 2019/5/31
 @Desc  :
"""
from flask import render_template, session

from app.view import web

@web.route("/project/testing")
def project_testing():
    return render_template("testing.html" ,info=session)