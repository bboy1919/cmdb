#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : zbhost.py
 @Author: Junyue
 @Date  : 2019/5/30
 @Desc  :
"""
from sqlalchemy import Column, String, Integer,ForeignKey
from sqlalchemy.orm import relationship

from .base import BaseNoCreateTime
class Zbhost(BaseNoCreateTime):
    __tablename__ = "zbhost"

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    cmdb_hostid = Column(Integer)
    hostid = Column(Integer)
    host = Column(String(40))
    ip = Column(String(30))

    def keys(self):
        return ["id", "cmdb_hostid", "hostid", "host", "ip"]