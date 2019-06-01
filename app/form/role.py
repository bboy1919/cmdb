#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : role.py
 @Author: Junyue
 @Date  : 2019/5/27
 @Desc  :
"""
from wtforms import StringField, PasswordField, Form, IntegerField, SelectMultipleField
from wtforms.validators import Length, Email, \
    ValidationError, EqualTo, DataRequired, Regexp

from app.model.role import Role


class UpdateRoleForm(Form):
    id = IntegerField()
    name = StringField("角色名", validators=[DataRequired(message="角色名不可为空"), Length(min=3)])
    name_cn = StringField("中文名", validators=[DataRequired(message="中文名不可为空"), Length(min=2)])
    info = StringField()
    p_id = SelectMultipleField('permission', choices=[], coerce=int, option_widget=None)


class AddRoleForm(UpdateRoleForm):
    def validate_name(self, field):
        if Role.query.filter(Role.name==field.data).first():
            raise ValidationError('角色名已存在')