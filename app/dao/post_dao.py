from app.dao.base_dao import BaseDAO
from app.dao.models.models import Post


class PostDAO(BaseDAO[Post]):
    __model__ = Post

    def get_item_by_username(self, username: str):
        all_items = self._db_session.query(self.__model__).filter(username == self.__model__.poster_name).all()

        return all_items

    def get_posts_by_word(self):
        all_items = self._db_session.query(self.__model__.content).all()

        return  all_items
