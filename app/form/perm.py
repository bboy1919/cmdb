#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : permission.py
 @Author: Junyue
 @Date  : 2019/5/27
 @Desc  :
"""
from wtforms import StringField, Form, IntegerField
from wtforms.validators import Length, DataRequired, URL, ValidationError

from app.model.permision import Permission


class UpdatePermForm(Form):
    id = IntegerField()
    name = StringField("角色名", validators=[DataRequired(message="角色名不可为空"), Length(min=3)])
    name_cn = StringField("中文名", validators=[DataRequired(message="中文名不可为空"), Length(min=2)])
    url = StringField("URL",validators=[URL(message="lllll")])
    comment = StringField()

    def validate_name(self, field):
        if Permission.query.filter(Permission.name == field.data).first():
            raise ValidationError('角色名已存在')
