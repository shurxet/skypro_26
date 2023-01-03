from typing import TypeVar, Generic, Optional

from sqlalchemy.orm import scoped_session
from app.dao.models.models import BaseModel


T = TypeVar('T', bound=BaseModel)


class BaseDAO(Generic[T]):
    __model__ = BaseModel

    def __init__(self, db_session: scoped_session) -> None:
        self._db_session = db_session

    def get_all(self) -> Optional[T]:
        all_items = self._db_session.query(self.__model__).all()

        return all_items

    def get_by_id(self, pk: int) -> Optional[T]:
        return self._db_session.query(self.__model__).get(pk)

    def update(self, data):
        self._db_session.add(data)
        self._db_session.commit()

        return data
