from flask import Flask


def create_app():
    """Initialises Flask application.
    """
    app = Flask(__name__)
    app.config['SECRET KEY'] = 'never share in production'
    return app
