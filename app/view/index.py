#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : index.py
 @Author: Junyue
 @Date  : 2019/5/18
 @Desc  :
"""
from flask import render_template, session, jsonify, redirect, url_for
from flask import request
from flask_login import login_required, current_user, logout_user


from app.lib.re_data import data_return
from ..model import db
from app.form.auth import PassForm, infoForm
from . import web
from app.model.user import User


@web.route("/",)
@login_required
def index():
    per = set()
    role_l = {}
    user = User.query.filter_by(id=current_user.id).first_or_404()
    u_res = dict(user)
    for role in u_res["role"]:
        per.update(role.permission)
        role_l[role.name] = role.name_cn
    perm_l = {perm.name:perm.name_cn for perm in per}
    session['user'] = u_res  # 用户信息存入session
    session['role'] = list(role_l.keys())  # 角色名eg:['sa','php']
    session['perm'] = list(perm_l.keys())  # 权限名eg:['git','mysql']
    session['username'] = user.username
    u_res["role"] = ",".join(list(role_l.values()))
    u_res["perm"] = ','.join(['<a href="%s" style="color:blue">%s</a>' % (x.url, x.name_cn) for x in per])

    return render_template("index.html",info=session,user=u_res)


@web.route("/user/chpwdoneself", methods=['POST'])
@login_required
def change_self_password():
    form = PassForm(request.form)
    user = User.query.filter_by(id=current_user.id).first()
    if form.validate():
        if user.check_password(form.oldpasswd.data):
            user.password = form.newpasswd.data
            db.session.commit()
            return data_return()
        return  data_return(errmsg=form.oldpasswd.errors,code=1)
    err = "/n".join(form.newpasswd.errors)
    return data_return(errmsg=err,code=1)


@web.route("/user/chgselfinfo", methods=['POST'])
@login_required
def change_self_info():
    user = User.query.filter_by(id=current_user.id).first()
    form = infoForm(request.form)
    if form.validate():
        with db.auto_commit():
            user.set_attrs(form.data)
        return data_return()
    err = "\n".join([v[0] for k,v in form.errors.items()])
    return data_return(errmsg=err,code=1)


@web.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('web.login'))