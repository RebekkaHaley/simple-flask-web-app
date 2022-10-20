"""Contains functions related to authentication.
"""

from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "<p>Logout successful</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password_one = request.form.get('password_one')
        password_two = request.form.get('password_two')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password_one != password_two:
            flash('Passwords must be equal.', category='error')
        elif len(password_one) < 7:
            flash('Password must be greater than 6 characters.', category='error')
        else:
            flash('Account created!', category='success')

    return render_template("sign_up.html")
