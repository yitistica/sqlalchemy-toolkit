import re
import decimal
import pandas as pd
from enum import Enum

from sqlalchemy import select, delete
from sqlalchemy.orm import Bundle


from sqlalchemy.sql.expression import Insert
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.schema import DDLElement


class TableCRUD(object):

    def __init__(self, session_cls, session_cls_kwargs=()):
        if not session_cls_kwargs:
            session_cls_kwargs = dict()

        self._session_cls = session_cls
        self._session_cls_kwargs = session_cls_kwargs

    def make_session(self):
        session = self._session_cls(**self._session_cls_kwargs)

        return session

    def execute(self, session, stmt):
        results = session.execute(stmt)

        return results
