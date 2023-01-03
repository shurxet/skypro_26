from app.dao.bookmark_dao import BookmarkDAO
from app.dao.models.models import Bookmark
from app.services.base_service import BaseService


class BookmarkService(BaseService[BookmarkDAO]):

    def get_all(self) -> list[Bookmark]:

        return self.dao.get_all()


    def add_bookmark(self, pid: int):

        self.dao.add_bookmarks(pid)


    def delete_bookmark(self, pid: int):

        bookmark = self.dao.get_by_id(pid)

        self.dao.delete_bookmarks(bookmark)





