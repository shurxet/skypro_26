from app.config import config
from app.config_db import db
from app.main import create_app

if __name__ == '__main__':
    with create_app(config).app_context():
        db.drop_all()
        db.create_all()
