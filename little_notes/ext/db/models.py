from flask_login import UserMixin

from little_notes.ext.db import db


class Note(db.Model):
    __tablename__ = "note"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text())
    created_at = db.Column(
        "created_at",
        db.DateTime(timezone=True),
        default=db.func.current_timestamp(),
    )
    updated_at = db.Column(
        "updated_at",
        db.DateTime(timezone=True),
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
    )
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return f"<User {self.id}>"

    def __str__(self):
        return str(self.id)


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    created_at = db.Column(
        "created_at",
        db.DateTime(timezone=True),
        default=db.func.current_timestamp(),
    )
    updated_at = db.Column(
        "updated_at",
        db.DateTime(timezone=True),
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
    )
    notes = db.relationship("Note")

    def __repr__(self):
        return f"<User {self.username}>"

    def __str__(self):
        return self.username
