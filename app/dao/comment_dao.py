from app.dao.base_dao import BaseDAO
from app.dao.models.models import Comment


class CommentDAO(BaseDAO[Comment]):
    __model__ = Comment

    def get_item_by_post_pk(self, pk: int):
        all_items = self._db_session.query(self.__model__).filter(pk == self.__model__.post_id).all()

        return all_items

