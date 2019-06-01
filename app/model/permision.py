#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : permision.py
 @Author: Junyue
 @Date  : 2019/5/18
 @Desc  :
"""

from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy import Integer,String
from sqlalchemy.orm import relationship


from .base import BaseNoCreateTime,db


role_o2m_permission = db.Table('role_o2m_permission',
                        Column('role_id',Integer,ForeignKey('role.id')),
                        Column('permission_id',Integer,ForeignKey('permission.id')),
                        )


class Permission(BaseNoCreateTime):
    __tablename__ = "permission"

    id = Column(Integer, nullable=False,autoincrement=True, primary_key=True)
    name = Column(String(32), nullable=False, unique=True)
    name_cn = Column(String(40), nullable=False)
    url = Column(String(128), nullable=False)
    comment = Column(String(128))

    role = relationship("Role", secondary=role_o2m_permission, backref='permission')

    def keys(self):
        return ["id","name_cn", "name", "url", "comment"]

    def __getitem__(self, item):
        return getattr(self,item)

    @classmethod
    def choiced_permission_item(cls, *args):
        return cls.query.filter(cls.id.in_(*args)).all()

    @classmethod
    def all_permission(cls, validator=True):
        """
        用于Form的SelectMultipleField——choice
        :param validator:
        :return:
        """
        if validator:
            return [[p.id, p.name] for p in cls.query.all()]
        return {p.id: p.name for p in cls.query.all()}

    @classmethod
    def select_list(cls,l):
        """
        生成多选框已选未选
        :param l:
        :return:
        """
        ps = {}
        for d_l in cls.query.all():
            if l and d_l.id in l:
                ps[d_l.id] = [d_l.name, 1]
            else:
                ps[d_l.id] = [d_l.name, 0]
        return ps

    @classmethod
    def choiced_permission_item(cls, *args):
        """
        查询已选id所对应得对象，用于关系表数据变更
        :param args:
        :return:
        """
        return cls.query.filter(cls.id.in_(*args)).all()