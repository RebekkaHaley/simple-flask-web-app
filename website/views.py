"""Contains the standard routes for the website, e.g., the home page.
"""

from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user

from . import db
from .models import Note

# NB: A 'Blueprint' has a bunch of URLs pre-defined.
views = Blueprint('views', __name__)


# NB: This function will run whenever we go to the '/' route.
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template("home.html", user=current_user)
