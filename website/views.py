"""Contains the standard routes for the website, e.g., the home page.
"""

from flask import Blueprint, render_template
from flask_login import login_required, current_user

# NB: A 'Blueprint' has a bunch of URLs pre-defined.
views = Blueprint('views', __name__)


# NB: This function will run whenever we go to the '/' route.
@views.route('/')
@login_required
def home():
    return render_template("home.html")
