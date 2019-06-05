#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : cabinet.py
 @Author: Junyue
 @Date  : 2019/5/28
 @Desc  :
"""
from flask import render_template, session, request
from flask_login import login_required

from app import db
from app.form.cabinet import AddCabinetForm, UpdateCabinetForm
from app.lib.re_data import data_return
from app.model.cabinet import Cabinet
from app.model.idc import Idc
from app.view import web
from app.lib.helper import model_serializable, err_list


@web.route("/cmdb/cabinet")
@login_required
def cabinet_index():
    return render_template("cabinet.html",info=session)


@web.route("/cmdb/getcabinet")
@login_required
def get_cabinet():
    res = []
    cab_list = Cabinet.query.all()
    for item in cab_list:
        res.append(model_serializable(item))
    return data_return(result=res)

@web.route("/cmdb/addcabinet", methods=["GET", "POST"])
@login_required
def add_cabinet():
    if request.method == "GET":
        res=[]
        res_list = Idc.query.all()
        for item in res_list:
            res.append(model_serializable(item))
        return data_return(result=res)
    r_cab = AddCabinetForm(request.form)
    if r_cab.validate():
        cab = Cabinet()
        with db.auto_commit():
            cab.set_attrs(r_cab.data)
            db.session.add(cab)
        return data_return()
    else:
        return data_return(code=1,errmsg=err_list(r_cab))


@web.route("/cmdb/updatecabinet", methods=["GET", "POST"])
@login_required
def update_cabinet():
    if request.method == "GET":
        id = request.args.get("id")
        update_cab = Cabinet.query.filter(Cabinet.id == id).first_or_404()
        res = model_serializable(update_cab)
        return data_return(result=res)

    r_cab = UpdateCabinetForm(request.form)
    id = r_cab.id.data
    if r_cab.validate():
        cab = Cabinet.query.filter(Cabinet.id == id).first_or_404()
        with db.auto_commit():
            cab.set_attrs(r_cab.data)
            db.session.add(cab)
        return data_return()
    else:
        return data_return(code=1, errmsg=err_list(r_cab))


@web.route("/cmdb/delcabinet")
@login_required
def del_cabinet():
    id = request.args.get("id")
    del_cab = Cabinet.query.filter(Cabinet.id == id).first_or_404()
    with db.auto_commit():
        db.session.delete(del_cab)
    return data_return()