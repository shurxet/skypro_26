from typing import TypeVar, Generic

from app.dao.base_dao import BaseDAO


T = TypeVar('T', bound=BaseDAO)


class BaseService(Generic[T]):

    def __init__(self, dao: T, *args, **kwargs):
        self.dao = dao