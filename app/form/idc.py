#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : idc.py
 @Author: Junyue
 @Date  : 2019/5/28
 @Desc  :
"""
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Email, DataRequired, Length, Regexp, ValidationError

from app.model.idc import Idc



class UpdateIdcForm(Form):
    id = IntegerField()
    name = StringField("IDC简称", validators=[DataRequired(message="名称不可为空"), Length(min=2, message="至少2个字符")])
    idc_name = StringField("IDC全名", validators=[DataRequired(message="名称不可为空"),
                                                Length(min=2, message="至少2个字符"),
                                                Regexp(regex="^[\u4e00-\u9fa5]{0,}$", message="必须中文字符")
                                                ])
    address = StringField("IDC地址", validators=[DataRequired(message="名称不可为空"), Length(min=2, message="至少2个字符")])
    phone = StringField("客服电话", validators=[DataRequired(message="输入电话号码非手机"),
                                            Regexp(regex="^1([38][0-9]|4[579]|5[0-3,5-9]|6[6]|7[0135678]|9[89])\d{8}$",
                                                   message='手机号码错误')
                                            ])
    email = StringField("邮件", validators=[DataRequired(message="邮箱不可为空"), Email(message='电子邮箱不符合规范')])
    user_interface = StringField("IDC接口人")
    user_phone = StringField("接口人电话", validators=[DataRequired("手机号不可为空"),
                                                  Regexp(
                                                      regex="^1([38][0-9]|4[579]|5[0-3,5-9]|6[6]|7[0135678]|9[89])\d{8}$",
                                                      message='手机号码错误')
                                                  ])
    rel_cabinet_num = StringField("实际机柜数", validators=[DataRequired(message="输入实际数据")])
    pact_cabinet_num = StringField("合同机柜数", validators=[DataRequired(message="输入合同数据")])


class IdcForm(UpdateIdcForm):

    def validate_name(self, field):
        if Idc.query.filter(Idc.name == field.data).first():
            raise ValidationError('IDC名已存在')