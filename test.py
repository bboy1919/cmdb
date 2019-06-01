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

from zabbix_client import ZabbixServerProxy

# s = ZabbixServerProxy('http://10.0.0.81/zabbix')
# t = s.apiinfo.version()
# print(t)

class Test1(object):


    def __init__(self, obj):
        print ("In __init__")
        self.data = obj


    def __str__(self):
        print ("In __str__")
        return str(self.data)


    __repr__ = __str__


    def get_attr(self):
        print ("In getattr")
        return self.data


    def __getattr__(self, attr):
        print("In __getattr__")
        return getattr(self.data, attr)


if __name__ == '__main__':
    myString = Test1('hello')
    print (myString)
    print (myString.upper())
    print (myString.get_attr())

