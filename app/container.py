from app.config_db import db
from app.dao.bookmark_dao import BookmarkDAO
from app.dao.comment_dao import CommentDAO
from app.dao.post_dao import PostDAO
from app.services.bookmark_service import BookmarkService
from app.services.comment_service import CommentService
from app.services.post_service import PostService


post_dao = PostDAO(db.session)
post_service = PostService(post_dao)

comment_dao = CommentDAO(db.session)
comment_service = CommentService(comment_dao)

bookmark_dao = BookmarkDAO(db.session)
bookmark_service = BookmarkService(bookmark_dao)
