#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : login.py
 @Author: Junyue
 @Date  : 2019/5/18
 @Desc  :
"""
from datetime import datetime

from flask import request,render_template,jsonify
from flask_login import login_user

from app import db
from app.form.auth import LoginForm
from app.lib.re_data import data_return
from app.view import web
from app.model.user import User


@web.route("/login", methods=['POST','GET'])
def login():

    if request.method == 'GET':
        return render_template("login.html")
    form = LoginForm(request.form)
    if form.validate():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.passwd.data):
            if user.is_lock == 1:
                res = {'code': 0, 'errmsg': "用户已被锁定"}
            else:
                with db.auto_commit():
                    user.last_login = int(datetime.now().timestamp())
                login_user(user, remember=False)
                res = {'code':0,'errmsg':'ok'}
        else:
            res = {'code': 1, 'errmsg': "用户名或密码错误"}
    else:
        err = [value[0] for key,value in form.errors.items()]
        res = {'code': 1, 'errmsg': "\n".join(err)}

    return data_return(**res)