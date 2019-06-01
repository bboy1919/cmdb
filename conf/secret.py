#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : secret.py
 @Author: Junyue
 @Date  : 2019/5/18
 @Desc  :
"""

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:kala1919@127.0.0.1:3306/cmdb'

SECRET_KEY = 'seeeeeeeeeeesef'

# 开启数据库查询性能测试
SQLALCHEMY_RECORD_QUERIES = True

# 性能测试的阀值
DATABASE_QUERY_TIMEOUT = 0.5

SQLALCHEMY_TRACK_MODIFICATIONS = True

WTF_CSRF_CHECK_DEFAULT = False

SQLALCHEMY_ECHO = False

from datetime import timedelta
REMEMBER_COOKIE_DURATION = timedelta(days=30)

ZABBIX_URL = "http://10.0.0.81/zabbix"
ZABBIX_USER = "Admin"
ZABBIX_PASSWORD = "zabbix"
ZABBIX_LOGIN_URL = "http://10.0.0.81/zabbix/index.php"
ZABBIX_GRAPH_URL = "http://10.0.0.81/zabbix/chart2.php"