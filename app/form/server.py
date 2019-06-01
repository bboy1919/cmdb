#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : server.py
 @Author: Junyue
 @Date  : 2019/5/29
 @Desc  :
"""

from wtforms import Form, StringField, IntegerField, DateField
from wtforms.validators import  DataRequired, Length, Regexp, ValidationError, IPAddress

from app.model.server import Server


class UpdateServerForm(Form):
    id = IntegerField()
    hostname = StringField("主机名",validators=[DataRequired(message="主机名必填")])
    ip = StringField("主机IP", validators=[IPAddress(message="ip不符合")])
    vm_status = IntegerField("VM_status")
    st = StringField("SN号")
    uuid = StringField("uid值")
    manufacturers = StringField("生产商")
    server_type = StringField("服务器型号")
    server_cpu = StringField("CPU型号")
    os = StringField("操作系统")
    server_disk = StringField("磁盘大小")
    server_mem = IntegerField("内存大小")
    mac_address = StringField("MAC地址")
    manufacture_date = DateField("生产日期")
    supplier = StringField("供应商")
    cab_id = IntegerField("所属机柜",validators=[DataRequired(message="请选所属机柜")])
    cab_pos = StringField("机柜位置")
    expire = DateField("机器到保日期")
    supplier_phone = StringField("联系供应商")
    server_up_time = DateField("机器上架日期")
    server_purpose = StringField("业务线")
    host = IntegerField("宿主机")
    server_run = StringField("服务线")
    host_status = IntegerField("主机状态")
    host_models = StringField("主机类型")


class AddServerForm(UpdateServerForm):

    def validate_hostname(self, field):
        if Server.query.filter(Server.hostname == field.data).first():
            raise ValidationError('设备已存在')
