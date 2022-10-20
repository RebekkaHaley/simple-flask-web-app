"""Contains Flask application.
"""

from flask import Flask


def create_app():
    """Initialises Flask application.
    """
    app = Flask(__name__)
    app.config['SECRET KEY'] = 'never share in production'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
