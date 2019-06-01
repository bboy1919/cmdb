#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : cobinet.py
 @Author: Junyue
 @Date  : 2019/5/28
 @Desc  :
"""
from sqlalchemy import Integer, String, Column,ForeignKey
from sqlalchemy.orm import relationship

from .base import BaseNoCreateTime

class Cabinet(BaseNoCreateTime):
    __tablename__ = "cabinet"

    id = Column(Integer,nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(30),nullable=False)
    idc_id = Column(Integer, ForeignKey('idc.id'))
    power = Column(String(20))

    idc = relationship("Idc", backref='cabinet')

    def keys(self):
        return ["id", "name", "power", "idc"]