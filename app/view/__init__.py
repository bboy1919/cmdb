#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : __init__.py.py
 @Author: Junyue
 @Date  : 2019/5/18
 @Desc  :
"""

from flask import Blueprint,session,request
from werkzeug.exceptions import HTTPException

from app.lib.c_exception import Forbidden
from app.lib.errors import APIException
from conf.setting import ZABBIX_ENABLE
from app.lib.casbin_api import enforcer
web = Blueprint('web', __name__, template_folder='templates')



from . import index
from .user import login
from .user import user
from .user import role
from .user import perm
from . import cobber_system
if ZABBIX_ENABLE:
    from . import zabbix
from .cmdb import server
from .cmdb import idc
from .cmdb import cabinet
from .cmdb import access
from .cmdb import switch

from .project import project
from .project import apply
from .project import deploy
from .project import testing



@web.app_errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(code=code, error_code=error_code, msg=msg)
    else:
        # if not app.config["DEBUG"]:
        #     return ServerError()
        # else:
        raise e

@web.before_request
def role_access_control():
    enforcer.load_policy()
    user = session.get("username", None)
    if user is None:
        user = 'anonymous'
    path = request.path
    method = request.method
    if enforcer.enforce(user, path, method):
        return None
    else:
        description = "没有权限访问改功能，请联系管理员"
        return Forbidden(msg=description)

