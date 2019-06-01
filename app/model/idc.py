#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : idc.py
 @Author: Junyue
 @Date  : 2019/5/28
 @Desc  :
"""
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer,String
from sqlalchemy.orm import relationship

from .base import BaseNoCreateTime,db
from .cabinet import Cabinet

class Idc(BaseNoCreateTime):
    __tablename__ = "idc"

    id = Column(Integer, nullable=False,primary_key=True,autoincrement=True)
    name = Column(String(20), nullable=False)
    idc_name = Column(String(30),nullable=False)
    address = Column(String(255),nullable=False)
    phone = Column(String(15),nullable=False)
    email = Column(String(30),nullable=False)
    user_interface = Column(String(50),nullable=False)
    user_phone = Column(String(20),nullable=False)
    rel_cabinet_num = Column(String(11))
    pact_cabinet_num = Column(String(11),nullable=False)



    def keys(self):
        return ["id","name", "idc_name", "address", "phone", "email",
                "user_interface", "user_phone", "rel_cabinet_num", "pact_cabinet_num"]