import dotenv
from flask import Flask
from app.views.main import main_blueprint
from app.config_db import db, migrate

from app.api.api import api_blueprint


def create_app(config_obj) -> Flask:
    app = Flask(__name__)
    dotenv.load_dotenv(override=True)
    app.config.from_object(config_obj)
    app.config.from_envvar("APP_SETTINGS", silent=True)
    app.app_context().push()
    db.init_app(app)
    with app.app_context():
        if db.engine.url.drivername == 'sqlite':
            migrate.init_app(app, db, render_as_batch=True)
        else:
            migrate.init_app(app, db)

    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_blueprint)

    return app

