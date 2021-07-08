import json

from flask import Blueprint, flash, jsonify, render_template, request
from flask_login import current_user, login_required

from little_notes.ext.db import db
from little_notes.ext.db.models import Note

blueprint = Blueprint("site", __name__)


@blueprint.route("/", methods=["GET"])
def index():
    return render_template("index.html", user=current_user)


@blueprint.route("/home/", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        text_note = request.form.get("note")
        if text_note == "":
            flash("note cannot be empty.", category="warning")
        else:
            new_note = Note(description=text_note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note created successfully!", category="success")
    return render_template("home.html", user=current_user)


@blueprint.route("/notes/delete", methods=["DELETE"])
@login_required
def delete_note():
    data = json.loads(request.data)
    note_id = data["note_id"]
    note = Note.query.get(note_id)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            flash("Note delete successfully!", category="success")
        else:
            flash("Note not found!", category="danger")
    return jsonify({})
