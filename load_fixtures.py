from contextlib import suppress
from typing import List, Dict, Any, Type


from sqlalchemy.exc import IntegrityError

from app.config import config
from app.config_db import db


from app.dao.models.models import BaseModel, Comment, Bookmark, Post
from app.main import create_app

from utils import read_json


def load_data(data: List[Dict[str, Any]], model: Type[BaseModel]) -> None:
    for item in data:
        item['id'] = item.pop('pk')
        db.session.add(model(**item))


if __name__ == '__main__':
    fixtures: Dict[str, List[Dict[str, Any]]] = read_json("fixtures.json")

    app = create_app(config)

    with app.app_context():
        load_data(fixtures['bookmarks'], Bookmark)
        with suppress(IntegrityError):
            db.session.commit()

    with app.app_context():
        load_data(fixtures['comments'], Comment)
        with suppress(IntegrityError):
            db.session.commit()

    with app.app_context():
        load_data(fixtures['posts'], Post)
        with suppress(IntegrityError):
            db.session.commit()
