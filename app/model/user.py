#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : user.py
 @Author: Junyue
 @Date  : 2019/5/18
 @Desc  :
"""
from flask_login import UserMixin
from sqlalchemy import Column, String, orm
from sqlalchemy import Integer
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from app import login_manager
from .base import Base



class User(UserMixin, Base):
    """

    """
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username = Column(String(40), nullable=False, unique=True)
    _password = Column('password', String(128))
    name = Column(String(80), nullable=False)
    mobile = Column(String(16))
    is_lock = Column(Integer, nullable=False)
    last_login = Column(Integer)


    def keys(self):
        return ["id","username", "name", "mobile", "is_lock", "role"]


    # @orm.reconstructor
    # def __init__(self):
    #     self.fields = ['id', 'username', 'name', 'mobile',
    #                    'publisher',
    #                    'is_lock']

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)

@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))