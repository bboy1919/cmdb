#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : manage.py
 @Author: Junyue
 @Date  : 2019/5/18
 @Desc  :
"""
import os

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from run_web import app
from app.model import db


migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()