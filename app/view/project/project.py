#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : project.py
 @Author: Junyue
 @Date  : 2019/5/31
 @Desc  :
"""
from flask import render_template, session

from app.view import web

@web.route("/project/project")
def project_index():
    return render_template("project.html" ,info=session)