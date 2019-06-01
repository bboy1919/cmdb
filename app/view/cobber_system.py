#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : cobber_system.py
 @Author: Junyue
 @Date  : 2019/5/21
 @Desc  :
"""
from flask import request, render_template, jsonify, session
from flask_login import login_required

from . import web
from app.model.permision import Permission

@web.route("/cobbler/system", methods=['GET','POST'])
@login_required
def sys_list():
    if request.method == "GET":
        return render_template("system.html", info=session)

    # result = []
    # res = {}
    # q_l = Permission.query.all()
    # for perm in q_l:
    #     tmp = {}
    #     tmp["id"] = perm.id
    #     tmp["name"] = perm.name
    #     tmp["url"] = perm.url
    #     tmp["comment"] = perm.comment
    #     result.append(tmp)
    #
    # res["code"] = 0
    # res["result"] = result
    # res["count"] = len(result)
    # return jsonify(res)