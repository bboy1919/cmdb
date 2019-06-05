#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : role.py
 @Author: Junyue
 @Date  : 2019/5/20
 @Desc  :
"""

from flask import request, render_template, jsonify, session
from flask_login import login_required

from app import db
from app.form.role import AddRoleForm, UpdateRoleForm
from app.lib.casbin_api import ret_all_groups, file_adapter, ret_all_policy
from app.lib.helper import model_serializable, err_list
from app.lib.re_data import data_return
from app.model.permision import Permission
from app.view import web
from app.model.role import Role

@web.route("/user/role")
@login_required
def role_list():
    return render_template("role.html", info=session)


@web.route("/user/roleinfo")
@login_required
def role_info():
    result = []
    r_l = Role.query.all()

    for role in r_l:
        res = model_serializable(role)
        res["permission"] = ",".join([p["name"] for p in res["permission"]])
        result.append(res)

    return data_return(result=result)


@web.route("/user/getrole")
@login_required
def get_role():
    uid = int(request.args.get("id"))
    role_item = Role.query.filter(Role.id==uid).first_or_404()
    e = model_serializable(role_item)
    return data_return(result=e)


@web.route("/user/getperm")
@login_required
def get_perm():
    id = request.args.get("id")
    if id:
        args = int(id)
        r = Role.query.filter(Role.id==args).first_or_404()
        perm_l = [p.id for p in r.permission]
        perm_l = Permission.select_list(perm_l)
    else:
        perm_l = Permission.all_permission(validator=False)
    return data_return(result=perm_l)


@web.route("/user/addrole", methods=["POST"])
@login_required
def add_role():
    res_data = request.form
    id = res_data.get("id")
    if id:
        r_data = UpdateRoleForm(request.form)
        role = Role.query.filter(Role.id==id).first_or_404()
    else:
        r_data = AddRoleForm(request.form)
        role = Role()

    r_data.p_id.choices = Permission.all_permission()
    ob_perm = Permission.choiced_permission_item(r_data.p_id.data)
    if r_data.validate():
        with db.auto_commit():
            role.set_attrs(r_data.data)
            role.permission = ob_perm
            db.session.add(role)

        # 添加角色权限到ACL
        ugp = []
        for p in ob_perm:
            ugp.append([p.url+"/*", "*"])
        update_group_policy = ret_all_policy()
        update_group_policy[role.name] = ugp
        file_adapter.change_policy("p", update_group_policy)

        return data_return()
    else:
        return data_return(code=1,errmsg=err_list(r_data))

@web.route("/user/delrole")
@login_required
def update_role():
    id = request.args.get("id")
    del_obj = Role.query.filter(Role.id == id).first()
    db.session.delete(del_obj)
    db.session.commit()
    return data_return()
