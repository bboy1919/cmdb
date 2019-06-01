#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : idc.py
 @Author: Junyue
 @Date  : 2019/5/28
 @Desc  :
"""
from flask import render_template, session, request

from app import db
from app.form.idc import IdcForm, UpdateIdcForm
from app.lib.re_data import data_return
from app.view import web
from app.model.idc import Idc
from app.lib.helper import model_serializable, err_list


@web.route("/cmdb/idc")
def idc_index():
    return render_template("idc.html",info=session)


@web.route("/cmdb/getidc", methods=["POST"])
def get_idc():
    res = []
    idc_list = Idc.query.all()
    for item in idc_list:
        res.append(model_serializable(item))
    return data_return(result=res)


@web.route("/cmdb/addidc", methods=["POST"])
def create_idc():
    res = IdcForm(request.form)
    if res.validate():
        idc = Idc()
        idc.set_attrs(res.data)
        with db.auto_commit():
            db.session.add(idc)
        return data_return()
    else:
        err = err_list(res)
        return data_return(code=1, errmsg=err)


@web.route("/cmdb/updateidc", methods=["GET","POST"])
def update_idc():
    if request.method == "GET":
        id = request.args.get("id")
        idc_item = Idc.query.filter(Idc.id == id).first_or_404()
        return data_return(result=model_serializable(idc_item))
    id = request.form.get("id")
    idc_item = Idc.query.filter(Idc.id == id).first_or_404()
    res_idc = UpdateIdcForm(request.form)
    if res_idc.validate():
        with db.auto_commit():
            idc_item.set_attrs(res_idc.data)
        return data_return()
    else:
        return data_return(code=1,errmsg= err_list(res_idc))


@web.route("/cmdb/delidc")
def del_idc():
    id = request.args.get("id")
    del_idc_item = Idc.query.filter(Idc.id == id).first_or_404()
    with db.auto_commit():
        db.session.delete(del_idc_item)
    return data_return()