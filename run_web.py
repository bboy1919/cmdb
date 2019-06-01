#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : run_web.py
 @Author: Junyue
 @Date  : 2019/5/18
 @Desc  :
"""
from app import create_app, db

app = create_app()
#
# with app.app_context():
#     db.create_all()

if __name__ == '__main__':
    app.run()
