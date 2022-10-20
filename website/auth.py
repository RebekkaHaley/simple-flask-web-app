"""Contains functions related to authentication.
"""

from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template("login.html", user="Jane Doe", boolean=True)


@auth.route('/logout')
def logout():
    return "<p>Logout successful</p>"


@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")
