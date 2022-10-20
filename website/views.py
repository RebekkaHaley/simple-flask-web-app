"""Contains the standard routes for the website, e.g., the home page.
"""

from flask import Blueprint

# NB: A 'Blueprint' has a bunch of URLs pre-defined.
views = Blueprint('views', __name__)


# NB: This function will run whenever we go to the '/' route.
@views.route('/')
def home():
    return "<h1>Home</h1>"
