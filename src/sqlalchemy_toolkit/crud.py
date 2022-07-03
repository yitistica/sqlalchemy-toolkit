from sqlalchemy import select, delete
from sqlalchemy.orm import Bundle


def auto_session(method):

    def crud(self, *args, **kwargs):

        session = self.make_session()
        session.begin()
        exception = None

        try:
            output = method(self, session, *args, **kwargs)
            session.commit()
        except Exception as e:
            exception = e
            session.rollback()
            output = None
        else:
            pass
        finally:
            session.close()

            if exception:
                raise exception

        return output

    return crud


class TableCRUD(object):

    def __init__(self, session_cls, session_cls_kwargs=()):
        if not session_cls_kwargs:
            session_cls_kwargs = dict()

        self._session_cls = session_cls
        self._session_cls_kwargs = session_cls_kwargs

    def make_session(self):
        session = self._session_cls(**self._session_cls_kwargs)

        return session

    @auto_session
    def create(self, session, model_cls, data):

        session.bulk_insert_mappings(
            model_cls, data,
            return_defaults=False)

        return True

    @auto_session
    def read(self, session, model_cls, columns=None, limit=None,
             return_dict=True):

        all_columns = model_cls.__table__.columns

        if not columns:
            columns = all_columns
        else:
            _columns = []
            for col in columns:
                if isinstance(col, str):
                    col = model_cls.__table__.columns[col]

                _columns.append(col)
            columns = _columns

        bundle = Bundle('all', *columns)

        if not limit:
            stmt = select(bundle)
        else:
            stmt = select(bundle).limit(limit)

        results = session.execute(stmt)

        if return_dict:
            column_names = [col.name for col in columns]

            for result in results:
                iter_result = dict(zip(column_names, result[0]))
                yield iter_result
        else:
            return results

    @auto_session
    def update(self, session, model_cls, data):

        session.bulk_update_mappings(
            model_cls, data)

        return True

    @auto_session
    def delete(self, session, model_cls, condition_clauses):

        stmt = delete(model_cls).where(*condition_clauses)
        results = session.execute(stmt)

        return results

    @auto_session
    def execute(self, session, stmt):
        results = session.execute(stmt)

        return results
