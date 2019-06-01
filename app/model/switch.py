#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : switch.py
 @Author: Junyue
 @Date  : 2019/5/28
 @Desc  :
"""
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.model.base import BaseNoCreateTime

class Switch(BaseNoCreateTime):
    __tablename__ = "switch"

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    ip = Column(String(50))
    device = Column(String(40), nullable=False)
    port = Column(Integer)
    cab_id = Column(Integer, ForeignKey("cabinet.id"))

    cabinet = relationship("Cabinet", backref='switch')

    def keys(self):
        return ["id", "ip", "device", "port", "cabinet"]