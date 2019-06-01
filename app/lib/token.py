#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : token.py
 @Author: Junyue
 @Date  : 2019/5/19
 @Desc  :
"""
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, \
    BadSignature

def generate_auth_token(id, name, rid,
                        expiration=7200):
    """生成令牌"""
    s = Serializer(current_app.config['SECRET_KEY'],
                   expires_in=expiration)
    return s.dumps({
        'id': id,
        'name': name,
        'rid':rid
    })