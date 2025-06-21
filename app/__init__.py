# app/__init__.py
import os
from flask import Flask
from .extensions import db
from .routes import api_bp
from .config import Config


def create_app():
    base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    app = Flask(
        __name__,
        template_folder=os.path.join(base_dir, 'templates'),
        static_folder=os.path.join(base_dir, 'static')
    )

    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(api_bp)

    with app.app_context():
        db.create_all()

    return app
