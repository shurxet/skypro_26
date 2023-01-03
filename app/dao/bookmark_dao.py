from app.dao.base_dao import BaseDAO
from app.dao.models.models import Bookmark, Post


class BookmarkDAO(BaseDAO[Bookmark]):
    __model__ = Bookmark

    def get_post_by_pk(self, pk: int) -> Post:
        return self._db_session.query(Post).get(pk)

    def add_bookmarks(self, pid):
        new_bookmark = Bookmark(
            post_id=pid,
        )

        self._db_session.add(new_bookmark)
        self._db_session.commit()

    def delete_bookmarks(self, post):
        self._db_session.delete(post)
        self._db_session.commit()


