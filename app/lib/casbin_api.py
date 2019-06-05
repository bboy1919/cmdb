#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : casbin_save.py
 @Author: Junyue
 @Date  : 2019/6/2
 @Desc  :
"""
import os
from functools import reduce

import casbin
from casbin import persist
from flask import current_app


class File_Adapter(persist.Adapter):
    _file_path = ""

    def __init__(self, file_path):
        self._file_path = file_path

    def load_policy(self, model):
        if not os.path.isfile(self._file_path):
            raise RuntimeError("invalid file path, file path cannot be empty")

        self._load_policy_file(model)

    def save_policy(self, model):
        pass

    def _load_policy_file(self, model):
        with open(self._file_path, "rb") as file:
            line = file.readline()
            while line:
                persist.load_policy_line(line.decode().strip(), model)
                line = file.readline()

    def _save_policy_file(self, text):
        with open(self._file_path, 'w') as f:
            f.write(text)


    def add_policy(self, sec, ptype, rule):
        pass

    def remove_policy(self, sec, ptype, rule):
        pass

    def remove_filtered_policy(self, sec, ptype, field_index, *field_values):
        pass


    def get_filtered_policy(self, ptype, all_type_item, sub):
        """
        去除控制列表里对应类型中所有条目中需要变更的项
        :param ptype:
        :param all_type_item: 控制列表里对应类型中所有条目
        :param sub: 需要变更的项
        :return:
        """
        policy = filter(lambda x:sub not in x, all_type_item)
        return list(map(lambda x:[ptype]+x, policy))

    def change_policy(self, ptype, *params):
        """
        对需要变更的项的策略进行组合，用于最后写入文件
        :param ptype:
        :param style: {type:all_type,sub:[[obj, act],[obj, act]]}
        :return:
        """
        if isinstance(params[0], dict):
            str_slice = params[0]
        else:
            pass
        all= str_slice[ptype]
        sub = list(str_slice.keys())[1]
        store_policy = self.get_filtered_policy(ptype, all, sub)

        # 生成变更项的规则条目
        for item in str_slice[sub]:
            store_policy.append([ptype, sub]+item)

        # 最后组合成所有的策略列表，用于文件写入
        if ptype == "g":
            all_other = [["p"]+py for py in enforcer.get_policy()]
            store_policy = all_other + store_policy
            store_policy.append(["g",sub,"anonymous"])
        else:
            all_other = [["g"]+gy for gy in enforcer.get_grouping_policy()]
            store_policy += all_other

        text = []
        for s in store_policy:
            text.append(", ".join(s))
        res = "\n".join(text)
        self._save_policy_file(res)


base_dir = os.getcwd()
file_adapter = File_Adapter(os.path.join(base_dir, "conf", "authz_policy.csv"))
enforcer = casbin.Enforcer(os.path.join(base_dir, "conf", "authz_model.conf"),file_adapter)

def ret_all_policy():
    all_policy = enforcer.get_policy()
    res = {"p": all_policy}
    return res

def ret_all_groups():
    all_groups = enforcer.get_grouping_policy()
    res = {"g": all_groups}
    return res


#
