#!/usr/bin/env python

"""
 @File  : auth.py
 @Author: Junyue
 @Date  : 2019/5/18
 @Desc  :
"""
from wtforms import StringField, PasswordField, Form, IntegerField, SelectMultipleField
from wtforms.validators import Length, Email, \
    ValidationError, EqualTo, DataRequired, Regexp

from app.model.user import User
from ..model.role import Role


class LoginForm(Form):
    username = StringField('用户名', validators=[
        DataRequired(message='用户名不可以为空'), Length(min=5, message='用户名长度必须大于%(min)d')])
    passwd = PasswordField('密码', validators=[
        DataRequired(message='密码不可以为空')])


class infoForm(Form):
    username = StringField('用户名', validators=[DataRequired("用户名不可为空"),
                                              Length(min=5, message='用户名长度必须大于%(min)d'),])
    name = StringField('姓名', validators=[DataRequired("姓名不可为空"),
                                         Length(min=2, message='用户名长度必须大于%(min)d')])
    mobile = StringField('手机号', validators=[DataRequired("手机号不可为空"),
        Regexp(regex="^1([38][0-9]|4[579]|5[0-3,5-9]|6[6]|7[0135678]|9[89])\d{8}$",
               message='手机号码错误')
    ])



class userForm(infoForm):
    id = IntegerField()
    is_lock = IntegerField()
    r_id = SelectMultipleField('roles', choices=[],coerce=int,  option_widget=None)




class PassForm(Form):
    oldpasswd = PasswordField('旧密码', validators=[
        DataRequired(message='密码不可以为空')])
    newpasswd = PasswordField('新密码', validators=[
        DataRequired(message='密码不可以为空'),
        Length(min=8, message='用户名长度必须大于%(min)d'),
        Regexp(regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}",
               message='密码至少8个字符，至少1个大写字母，1个小写字母，1个数字和1个特殊字符')])


class new_user_Form(userForm):
    password = PasswordField('旧密码', validators=[
        DataRequired(message='密码不可以为空'),EqualTo('repwd', message='两次输入的密码不一致')])
    repwd =PasswordField('旧密码', validators=[
        DataRequired(message='确认密码不可以为空'),])

    def validate_username(self, field):
        if User.query.filter(User.username == field.data).first():
            raise ValidationError('用户名已存在')