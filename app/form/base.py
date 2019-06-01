#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : base.py
 @Author: Junyue
 @Date  : 2019/5/26
 @Desc  :
"""
from flask_wtf import Form

from app.lib.c_exception import ParameterException


class BaseForm(Form):

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            # form errors
            raise ParameterException(msg=self.errors)
        return self