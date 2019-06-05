#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : server.py
 @Author: Junyue
 @Date  : 2019/5/28
 @Desc  :
"""
from flask import render_template, session, request
from flask_login import login_required

from app import db
from app.form.server import AddServerForm, UpdateServerForm
from app.lib.helper import model_serializable, err_list
from app.lib.re_data import data_return
from app.model.cabinet import Cabinet
from app.model.server import Server
from app.view import web

@web.route("/cmdb/server")
@login_required
def serv_index():
    return render_template("server.html", info=session)

@web.route("/cmdb/getserver")
@login_required
def get_server():
    get_s = Server.query.all()
    res_s = [model_serializable(s) for s in get_s]
    return data_return(result=res_s)


@web.route("/cmdb/addserver", methods=["POST", "GET"])
@login_required
def add_server():
    if request.method == "GET":
        """
        获取所有机柜信息
        """
        all_cab = Cabinet.query.all()
        res = [model_serializable(c) for c in all_cab]
        return data_return(result=res)

    add_server_form = AddServerForm(request.form)
    if add_server_form.validate():
        serv = Server()
        with db.auto_commit():
            serv.set_attrs(add_server_form.data)
            db.session.add(serv)
        return data_return()
    else:
        return data_return(code=1,errmsg=err_list(add_server_form))


@web.route("/cmdb/updateserver", methods=["POST", "GET"])
@login_required
def update_server():
    if request.method == "GET":
        id = request.args.get("id")
        s_item = Server.query.filter(Server.id == id).first_or_404()
        res = model_serializable(s_item)
        return data_return(result=res)
    res_s = UpdateServerForm(request.form)
    if res_s.validate():
        id = res_s.id.data
        update_s = Server.query.filter(Server.id==id).first_or_404()
        with db.auto_commit():
            update_s.set_attrs(res_s.data)
        return data_return()
    else:
        return data_return(code=1,errmsg=err_list(res_s))

