#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : zabbix_action.py
 @Author: Junyue
 @Date  : 2019/5/30
 @Desc  :
"""
from .zabbix_api import *

def get_host_group():
    hostgroup = zb.get_hostgroup()
    pass