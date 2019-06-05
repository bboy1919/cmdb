#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : test.py
 @Author: Junyue
 @Date  : 2019/5/19
 @Desc  :
"""
from datetime import datetime
import json
# x={}
# from werkzeug.security import generate_password_hash
# create_time =int(datetime.now().timestamp())
# t = generate_password_hash("Kala1919")
# for i in range(10):
#     for j in range(4):
#         x[i][j] = "d"
# if 1 in x.keys():
#     print(x)
# else:
#     print(x.keys())
# rpc_request = {
#         'jsonrpc': '2.0',
#         'id': '2',
#         'method': 'method'
#     }
# dump = json.dumps(rpc_request, separators=(',', ':'))
# print(dump)


import json

# s = ZabbixServerProxy('http://10.0.0.81/zabbix')
# t = s.apiinfo.version()
# print(t)

import nltk

aa = r'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>404</title>
</head>
<body>
你的权限不足，请联系管理员......                                                                         
</body>
</html>'''

print (nltk.clean_html(aa))