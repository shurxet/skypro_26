from app.dao.comment_dao import CommentDAO
from app.services.base_service import BaseService


class CommentService(BaseService[CommentDAO]):

    def get_by_pk(self, pk: int):
        all_items = self.dao.get_item_by_post_pk(pk)

        return all_items
