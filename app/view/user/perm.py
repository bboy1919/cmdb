#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : permission.py
 @Author: Junyue
 @Date  : 2019/5/21
 @Desc  :
"""

from flask import request, render_template, jsonify, session
from flask_login import login_required

from app import db
from app.form.perm import UpdatePermForm
from app.lib.helper import err_list, model_serializable
from app.lib.re_data import data_return
from app.view import web
from app.model.permision import Permission

@web.route("/user/power", methods=['GET','POST'])
@login_required
def perm_list():
    if request.method == "GET":
        return render_template("power.html", info=session)

    result = []
    # res = {}
    q_l = Permission.query.all()
    for perm in q_l:
        res = model_serializable(perm)
        result.append(res)

    return data_return(result=result)

@web.route("/perm/getperm", methods=["GET","POST"])
@login_required
def got_perm():
    uid = int(request.args.get("id"))
    perm_item = Permission.query.filter(Permission.id==uid).first_or_404()
    e = model_serializable(perm_item)
    return data_return(result=e)

@web.route("/perm/addperm", methods=["POST"])
def add_permission():
    res_data = request.form
    id = res_data.get("id")
    if id:
        perm = Permission.query.filter(Permission.id == id).first_or_404()
    else:
        perm = Permission()
    p_data = UpdatePermForm(request.form)
    if p_data.validate():
        with db.auto_commit():
            perm.set_attrs(p_data.data)
            db.session.add(perm)
        return data_return()
    else:
        return data_return(code=1, errmsg=err_list(p_data))


@web.route("/perm/delperm")
def del_perm():
    id = int(request.args.get("id"))
    delitem = Permission.query.filter(Permission.id == id).first_or_404()
    with db.auto_commit():
        db.session.delete(delitem)
    return data_return()