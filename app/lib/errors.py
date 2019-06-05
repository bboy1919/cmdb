#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : errors.py
 @Author: Junyue
 @Date  : 2019/5/26
 @Desc  :
"""
import json

from flask import request
from flask_login._compat import text_type
from werkzeug.exceptions import HTTPException
from werkzeug.utils import escape


class APIException(HTTPException):
    code = 500
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 999

    def __init__(self, msg=None, code=None, error_code=None,
                 headers=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None):
        body= text_type(
            (
                u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n'
                u"<title>%(code)s</title>\n"
                u"<h1>%(err_code)s</h1>\n"
                u"%(description)s\n"
            )
            % {
                "code": self.code,
                "err_code": self.error_code,
                "description": self.get_description(environ),
            }
        )
        return body

    def get_headers(self, environ=None):
        """Get a list of headers."""
        return [('Content-Type', 'text/html; charset=utf-8')]

    def get_description(self, environ=None):
        """Get the description."""
        return u"<p>%s</p>" % escape(self.msg)

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]