from marshmallow import Schema, fields
from sqlalchemy import Column, Integer, DateTime, String, func, ForeignKey
from sqlalchemy.orm import relationship

from app.config_db import db


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, nullable=False, default=func.now())
    updated = Column(DateTime, default=func.now(), onupdate=func.now())


class Post(BaseModel):
    __tablename__ = 'posts'

    poster_name = Column(String(1000), unique=False, nullable=False)
    poster_avatar = Column(String(1000), nullable=False)
    pic = Column(String(1000), nullable=False)
    content = Column(String(1000), nullable=False)
    views_count = Column(Integer, nullable=False)
    likes_count = Column(Integer, nullable=False)
    text_tag = Column(String(1000), nullable=True)
    content_tag = Column(String(1000), nullable=True)


class Bookmark(BaseModel):
    __tablename__ = 'bookmarks'

    post_id = Column(Integer, ForeignKey("posts.id", ondelete='CASCADE'))
    post = relationship("Post")


class Comment(BaseModel):
    __tablename__ = 'comments'

    post_id = Column(Integer, nullable=False)
    commenter_name = Column(String(1000), nullable=False)
    comment = Column(String(1000), nullable=False)


class PostSchema(Schema):
    id = fields.Int()
    poster_name = fields.Str()
    poster_avatar = fields.Str()
    pic = fields.Str()
    content = fields.Str()
    views_count = fields.Int()
    likes_count = fields.Int()
    text_tag = fields.Str()
    content_tag = fields.Str()




