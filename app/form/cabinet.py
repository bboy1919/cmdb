#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : cabinet.py
 @Author: Junyue
 @Date  : 2019/5/28
 @Desc  :
"""

from wtforms import Form, StringField, IntegerField
from wtforms.validators import Email, DataRequired, Length, Regexp, ValidationError

from app.model.cabinet import Cabinet

class UpdateCabinetForm(Form):
    id = IntegerField()
    name = StringField("机柜编号", validators=[DataRequired(message="请输入编号")])
    idc_id = IntegerField("所属IDC", validators=[DataRequired(message="请选所属IDC")])
    power = StringField("机柜功率")


class AddCabinetForm(UpdateCabinetForm):
    def validate_name(self, field):
        if Cabinet.query.filter(Cabinet.name == field.data).first():
            raise ValidationError('机柜编号已存在')