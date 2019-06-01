#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : user.py
 @Author: Junyue
 @Date  : 2019/5/20
 @Desc  :
"""

from flask import render_template, jsonify, request, session
from flask_login import login_required

from app.lib.helper import model_serializable, err_list
from app.lib.re_data import data_return
from app.model import db
from app.form.auth import userForm, new_user_Form
from app.model.role import Role
from app.view import web
from app.model.user import User

@web.route("/user/userinfo")
@login_required
def user_info():
    pass


@web.route("/user/userlist", methods=['GET', 'POST'])
@login_required
def user_list():
    result = []
    if request.method == 'POST':
        user_l = User.query.filter_by().all()
        for u in user_l:
            # user_one = {}
            # user_one["id"] = u.id
            # user_one["username"]=u.username
            # user_one["is_lock"]=u.is_lock
            # user_one["name"]=u.name
            # user_one["mobile"]=u.mobile
            # user_one["r_id"]=[r.id for r in u.role]
            # for r in u.role:
            #     user_one["r_id"].append(r.id)
            res = model_serializable(u)
            res["role"] = ",".join([r["name"] for r in res["role"]])
            result.append(res)

        return data_return(result=result)
    return render_template("userlist.html", info=session)


@web.route("/user/changeuserinfo")
@login_required
def change_user_info():
    uid = int(request.args.get("id"))
    user = User.query.filter_by(id=uid).first_or_404()
    if user:
        # res["id"]=user.id
        # res["name"]=user.name
        # res["username"]=user.username
        # res["mobile"]=user.mobile
        # res["is_lock"]=user.is_lock
        # at =[r.id for r in user.role]
        # for r_l in Role.query.all():
        #     if at and r_l.id in at:
        #         ps[r_l.id] = [r_l.name, 1]
        #     else:
        #         ps[r_l.id] = [r_l.name, 0]
        res = model_serializable(user)
        r_id = [r["id"] for r in res["role"]]
        res["role"]= Role.select_list(r_id)
        return data_return(result=res)
    return data_return(code=1, errmsg="用户不存在")


@web.route("/user/updateuserinfo", methods=['POST'])
@login_required
def update_user_info():
    info = userForm(request.form)
    info.r_id.choices = Role.all_roles()
    es = Role.choiced_role_item(info.r_id.data)
    if info.validate():
        ob_user = User.query.filter_by(id=info.id.data).first()
        with db.auto_commit():
            ob_user.set_attrs(info.data)
            ob_user.role = es
        return data_return()
    err = "\n".join([v[0] for k, v in info.errors.items()])
    return data_return(code=1,errmsg=err)


@web.route("/user/changeuserpasswd", methods=["POST"])
@login_required
def change_user_passwd():
    password_form = dict(request.form)
    id = password_form["passwdid"]
    password = password_form["changepasswd"]
    ch_password_user = User.query.filter_by(id=id).first()
    ch_password_user.password = password
    db.session.commit()
    return data_return()


@web.route("/user/adduser", methods=["GET","POST"])
@login_required
def add_user():

    if request.method == "GET":
        result = Role.all_roles(validator=False)
        return jsonify({"code": 0, "result": result})

    add_item = new_user_Form(request.form)
    add_item.r_id.choices = Role.all_roles()
    es = Role.choiced_role_item(add_item.r_id.data)
    if add_item.validate():
        user = User()
        with db.auto_commit():
            user.set_attrs(add_item.data)
            user.role = es
            db.session.add(user)
        return data_return()
    return data_return(code=1,errmsg=err_list(add_item))


@web.route("/user/deluser",)
@login_required
def del_user():
    id = request.args.get("id")
    User.query.filter_by(id=id).first().delete()
    db.session.commit()
    return data_return()