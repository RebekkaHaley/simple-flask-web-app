"""Contains Flask application.
"""

from os import path
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

log = logging.getLogger("website")
db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    """Initialises Flask application.
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'never share in production'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from . import models

    # Checks if a database already exists
    with app.app_context():
        db.create_all()

    return app
