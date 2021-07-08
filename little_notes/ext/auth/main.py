from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from little_notes.ext.db import db
from little_notes.ext.db.models import User

blueprint = Blueprint("auth", __name__)


@blueprint.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if len(email) < 4:
            flash("Email must be greater than 4 characters.", category="error")
        elif len(password) < 8:
            flash("Password must be at least 8 characters.", category="error")
        else:
            user = User.query.filter_by(email=email).first()
            if user:
                if check_password_hash(user.password, password):
                    flash("Logged in successfully", category="success")
                    login_user(user, remember=True)
                    return redirect(url_for("site.home"))
                else:
                    flash("Incorrect password.", category="error")
            else:
                flash("Email does not exist.", category="error")

    return render_template("login.html", user=current_user)


@blueprint.route("/logout/", methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@blueprint.route("/sign-up/", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists..", category="error")
        elif len(email) < 4:
            flash("Email must be greater than 4 characters.", category="error")
        elif len(username) < 4:
            flash(
                "First name must be greater than 4 characters.",
                category="error",
            )
        elif password1 != password2:
            flash("Passwords dn't match.", category="error")
        elif len(password1) < 8:
            flash("Password must be at least 8 characters.", category="error")
        else:
            new_user = User(
                username=username,
                email=email,
                password=generate_password_hash(password1, method="sha256"),
            )
            db.session.add(new_user)
            db.session.commit()
            flash("Account created!.", category="success")
            return redirect(url_for("auth.login"))

    return render_template("sign_up.html", user=current_user)


@blueprint.route("/profile/", methods=["GET"])
def profile():
    return "profile"
