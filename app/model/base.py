#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @File  : Base.py
 @Author: Junyue
 @Date  : 2019/5/18
 @Desc  :
"""
from datetime import datetime
from contextlib import contextmanager
from sqlalchemy import Column, Integer, SmallInteger
from flask import current_app
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from flask_sqlalchemy import BaseQuery

# from app.lib.c_exception import NotFound

__all__ = ['db', 'Base']


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self, throw=True):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            current_app.logger.exception('%r' % e)
            if throw:
                raise e


class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)

    # def get_or_404(self, ident):
    #     rv = self.get(ident)
    #     if not rv:
    #         raise NotFound()
    #     return rv
    #
    # def first_or_404(self):
    #     rv = self.first()
    #     if not rv:
    #         raise NotFound()
    #     return rv


db = SQLAlchemy(query_class=Query)


# class BaseMixin(object):
#     def __getitem__(self, key):
#         return getattr(self, key)


class Base(db.Model):
    __abstract__ = True
    join_date = Column('join_date', Integer)
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.join_date = int(datetime.now().timestamp())

    @property
    def create_datetime(self):
        if self.join_date:
            return datetime.fromtimestamp(self.join_date)
        else:
            return None

    def __getitem__(self, item):
        return getattr(self,item)

    def delete(self):
        self.status = 0

    def set_attrs(self, attrs):
        for key, value in attrs.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)


class BaseNoCreateTime(db.Model):
    __abstract__ = True


    def __getitem__(self, item):
        return getattr(self,item)

    def set_attrs(self, attrs):
        for key, value in attrs.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)
        return self