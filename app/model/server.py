#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : server.py
 @Author: Junyue
 @Date  : 2019/5/28
 @Desc  :
"""
from sqlalchemy import Column, String, Integer, ForeignKey, DATE
from sqlalchemy.orm import relationship

from app.model.base import BaseNoCreateTime

class Server(BaseNoCreateTime):
    __tablename__ = "server"

    id = Column(Integer,nullable=False, autoincrement=True, primary_key=True)
    hostname = Column(String(20))
    ip = Column(String(20))
    vm_status = Column(Integer)
    st = Column(String(50))
    uuid = Column(String(100))
    manufacturers = Column(String(100))
    server_type = Column(String(200))
    server_cpu = Column(String(200))
    os = Column(String(30))
    server_disk = Column(String(20))
    server_mem = Column(Integer)
    mac_address = Column(String(30))
    manufacture_date = Column(DATE)
    supplier = Column(String(30))
    cab_id = Column(Integer, ForeignKey("cabinet.id"))
    cab_pos = Column(String(10))
    expire = Column(DATE)
    supplier_phone = Column(String(20))
    server_up_time = Column(DATE)
    server_purpose = Column(String(30))
    host = Column(Integer)
    server_run = Column(String(30))
    host_status = Column(Integer, default=1)
    host_models = Column(String(10), default='1U')

    cabinet = relationship("Cabinet", backref='server')

    def keys(self):
        return ["id", "hostname", "ip", "vm_status", "st", "uuid", "manufacturers",
                "server_type", "server_cpu", "os", "server_disk", "server_mem",
                "mac_address", "manufacture_date", "supplier", "cab_pos",
                "cabinet", "expire", "supplier_phone", "server_up_time", "server_purpose",
                "host", "server_run", "host_status", "host_models"]