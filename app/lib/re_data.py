#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : re_data.py
 @Author: Junyue
 @Date  : 2019/5/26
 @Desc  :
"""
import json

from flask import jsonify


class ReturnData():
    code = 0
    result = ""
    errmsg = "ok"

    def __init__(self, code=None, result=None, errmsg=None):
        if code:
            self.code = code
        if result:
            self.result = result
        if errmsg:
            self.errmsg = errmsg


    def __getitem__(self, item):
        return getattr(self,item)

    def keys(self):
        return ["code","result", "errmsg"]

def data_return(**kwargs):
    r = dict(ReturnData(**kwargs))
    return jsonify(r)
