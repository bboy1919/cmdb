#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : zabbix.py
 @Author: Junyue
 @Date  : 2019/5/24
 @Desc  :
"""
from flask import render_template, request, json, session

from app.lib.re_data import data_return
from . import web
from app.lib.helper import model_serializable
from app.lib.zabbix_api import *

@web.route("/zabbix/jigui")
def zabbix_jigui():
    return render_template("jigui.html", info=session)

@web.route("/zabbix/getjigui")
def get_jigui():
    res = []
    server_list = Server.query.all()
    for item in server_list:
        server_item = model_serializable(item)
        server_item["cabinet_name"] = server_item["cabinet"]["name"]
        server_item["idc_name"] = server_item["cabinet"]["idc"]["name"]
        res.append(server_item)
    return data_return(result=res)

@web.route("/zabbix/template")
def zabbix_template():
    return render_template("template.html" ,info=session)

@web.route("/zabbix/maintenance")
def zabbix_maintenance():
    return render_template("maintenance.html",  info=session)



@web.route("/zabbix/gethostgroup")
def get_host_group():
    hostgroup = zb.get_hostgroup()
    return  data_return(result=hostgroup)

@web.route("/zabbix/gethost")
def get_host():
    init()
    zabbix_hosts = Zbhost.query.all()
    hostid = [zb.cmdb_hostid if zb.cmdb_hostid else 0 for zb in zabbix_hosts]
    server_hosts = [sh.id for sh in Server.query.all()]

    get_ip = Server.query.with_entities(Server.id, Server.ip).filter(~Server.id.in_(hostid)).all()
    get_ip = dict(get_ip)
    return data_return(result=get_ip)

@web.route("/zabbix/createhost", methods=["POST"])
def create_z_host():
    post_data = request.get_data()
    post_data = json.loads(post_data)
    create_zabbix_host(post_data["hostids"], post_data['groupid'])
    return data_return()

@web.route("/zabbix/gettemlist")
def get_tem_list():
    temp = zb.get_template()
    return data_return(result=temp)

@web.route("/zabbix/getzballhost")
def get_zb_all_host():
    data = zb.get_hosts()
    return data_return(result=data)

@web.route("/zabbix/getzabbixtem")
def get_zb_tem():
    data = zb.get_host_tem()
    return data_return(result=data)
