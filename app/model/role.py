#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : auth.py
 @Author: Junyue
 @Date  : 2019/5/18
 @Desc  :
"""
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer,String
from sqlalchemy.orm import relationship

from .base import BaseNoCreateTime,db



user_o2m_role = db.Table('user_o2m_role',
                        Column('u_id',Integer,ForeignKey('user.id')),
                        Column('r_id',Integer,ForeignKey('role.id')),
                        )

class Role(BaseNoCreateTime):
    __tablename__ = "role"

    id = Column(Integer, nullable=False,autoincrement=True, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    name_cn = Column(String(40), nullable=False)
    info = Column(String(50))

    user = relationship("User", secondary=user_o2m_role, backref='role')

    def keys(self):
        return ["id","name_cn", "name", "info", "permission"]


    @classmethod
    def all_roles(cls,validator=True):
        """
        用于Form的SelectMultipleField——choice
        :param validator:
        :return:
        """
        if validator:
            return [[r.id, r.name] for r in cls.query.all()]
        return {r.id:r.name for r in cls.query.all()}

    @classmethod
    def choiced_role_item(cls,*args):
        return cls.query.filter(cls.id.in_(*args)).all()

    @classmethod
    def select_list(cls,l):
        """

        :param l: 多选框选择项
        :return:
        """
        ps = {}
        for d_l in cls.query.all():
            if l and d_l.id in l:
                ps[d_l.id] = [d_l.name, 1]
            else:
                ps[d_l.id] = [d_l.name, 0]
        return ps