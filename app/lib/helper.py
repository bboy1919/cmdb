#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : se.py
 @Author: Junyue
 @Date  : 2019/5/26
 @Desc  :
"""
from datetime import datetime, date


def model_serializable(o):
    """
    单一模型对象多表关联链式序列化
    :param o:
    :return:
    """
    res = {}
    keys = o.keys()
    for key in keys:
        # print(type(o[key]))

        if isinstance(o[key],date):
            res[key] = datetime.strftime(o[key], "%Y-%m-%d")
        elif isinstance(o[key],int) or isinstance(o[key],str):
            res[key] = o[key]
        elif not o[key]:
            res[key] = ""
        elif isinstance(o[key],list):
            res[key] = [model_serializable(item) for item in o[key]]
        else:
            res[key] = model_serializable(o[key])

    return res

def err_list(f_err):
    return "\n".join([v[0] for k, v in f_err.errors.items()])