#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : switch.py
 @Author: Junyue
 @Date  : 2019/5/28
 @Desc  :
"""
from flask import render_template, session, request

from app import db
from app.form.switch import AddSwitchForm, UpdateSwitchForm
from app.lib.re_data import data_return
from app.model.cabinet import Cabinet
from app.model.switch import Switch
from app.view import web
from app.lib.helper import model_serializable, err_list


@web.route("/cmdb/switch")
def switch_index():
    return render_template("switch.html",info=session)


@web.route("/cmdb/getswitch")
def get_switch():
    all_switch_item = Switch.query.all()
    result = [model_serializable(s) for s in all_switch_item]
    return data_return(result=result)


@web.route("/cmdb/addswitch", methods=["POST","GET"])
def add_switch():
    if request.method == "GET":
        """
        获取所有机柜信息
        """
        all_cab = Cabinet.query.all()
        res = [model_serializable(c) for c in all_cab]
        return data_return(result=res)

    res_switch = AddSwitchForm(request.form)
    if res_switch.validate():
        with db.auto_commit():
            sw = Switch()
            sw.set_attrs(res_switch.data)
            db.session.add(sw)
        return data_return()
    else:
        return data_return(code=1, errmsg=err_list(res_switch))


@web.route("/cmdb/updateswitch", methods=["POST", "GET"])
def update_switch():
    if request.method == "GET":
        id = request.args.get("id")
        get_sw = Switch.query.filter(Switch.id == id).first_or_404()
        return data_return(result=model_serializable(get_sw))

    update_s = UpdateSwitchForm(request.form)
    if update_s.validate():
        id = update_s.id.data
        update_sw = Switch.query.filter(Switch.id==id).first_or_404()
        with db.auto_commit():
            update_sw.set_attrs(update_s.data)
        return data_return()


@web.route("/cmdb/delswitch")
def del_switch():
    id = request.args.get("id")
    del_sw = Switch.query.filter(Switch.id==id).first_or_404()
    with db.auto_commit():
        db.session.delete(del_sw)
    return data_return()