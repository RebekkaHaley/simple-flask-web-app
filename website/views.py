"""Contains the standard routes for the website, e.g., the home page.
"""

import json
from flask import Blueprint, render_template, request, flash, jsonify
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


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note_request = json.loads(request.data)
    note_id = note_request['noteId']
    note = Note.query.get(note_id)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
        else:
            flash('This note does not belong to you!', category='error')
    else:
        flash('Note does not exist!', category='error')
    return jsonify({})
