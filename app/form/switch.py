#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : switch.py
 @Author: Junyue
 @Date  : 2019/5/29
 @Desc  :
"""

from wtforms import Form, StringField, IntegerField
from wtforms.validators import Email, DataRequired, Length, Regexp, ValidationError, IPAddress

from app.model.switch import Switch

class UpdateSwitchForm(Form):
    id = IntegerField()
    ip = StringField("管理IP", validators=[IPAddress(message="IP不符合")])
    device = StringField("设备型号", validators=[DataRequired(message="请输入设备型号")])
    port = StringField("端口")
    cab_id = IntegerField("所属机柜")


class AddSwitchForm(UpdateSwitchForm):
    def validate_device(self, field):
        if Switch.query.filter(Switch.device == field.data).first():
            raise ValidationError('设备已存在')