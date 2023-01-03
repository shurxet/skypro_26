from flask import Blueprint

from app.container import post_service
from app.dao.models.models import PostSchema
import logging


logging.basicConfig(
        encoding='utf-8',
        level=logging.INFO,
        filename="logs/api.log",
        format='%(asctime)s [%(levelname)s] %(message)s')


api_blueprint = Blueprint("api", __name__)

posts_schema = PostSchema(many=True)
post_schema = PostSchema()

@api_blueprint.route('/api/posts/')
def api_posts():
    data = post_service.get_all()
    logging.info(f"запрос данных /api/posts/")
    return posts_schema.dump(data)


@api_blueprint.route('/api/posts/<int:post_id>')
def api_post(post_id):

    data = post_service.get_item(post_id)
    logging.info(f"запрос данных /api/posts/{post_id}")
    return post_schema.dump(data)
