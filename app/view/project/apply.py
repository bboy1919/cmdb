#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : apply.py
 @Author: Junyue
 @Date  : 2019/5/31
 @Desc  :
"""
from flask import render_template, session

from app.view import web

@web.route("/project/apply")
def apply_index():
    return render_template("apply.html" ,info=session)