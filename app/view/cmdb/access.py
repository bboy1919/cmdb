#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : access.py
 @Author: Junyue
 @Date  : 2019/5/28
 @Desc  :
"""
from flask import render_template, session, request

from app import db
from app.form.idc import IdcForm
from app.lib.re_data import data_return
from app.view import web
from app.model.idc import Idc
from app.lib.helper import model_serializable, err_list


@web.route("/cmdb/access")
def access_index():
    return render_template("access.html",info=session)