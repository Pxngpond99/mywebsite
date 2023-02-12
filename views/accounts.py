from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, login_user, logout_user

from werkzeug.security import generate_password_hash, check_password_hash

import models
from models import users, folios
from forms import accounts as accounts_form


bp = Blueprint("accounts", __name__, url_prefix="/accounts")


@bp.route("/login")
def login():
    form = accounts_form.LoginForm()
    return render_template("/accounts/login.html",form=form)

@bp.route("/logout")
def logout():
    logout_user()
    return redirect("/")



@bp.route("/do-login", methods=["POST"])
def do_login():

    form = accounts_form.LoginForm()

    if not form.validate_on_submit():
        return redirect(url_for("accounts.login", **form.errors))

    user = (
        models.db.session.query(users.User)
        .filter_by(
            email=form.email.data,
        )
        .first()
    )

    if not user:
        return redirect(url_for("accounts.login", message="invalid login"))

    if not check_password_hash(user.password, form.password.data):
        return redirect(url_for("accounts.login", message="invalid password"))

    login_user(user)

    return redirect(url_for("accounts.dashboard"))

@bp.route("/open_profile")
def open_profile():
    return render_template("/main/profile.html")


@bp.route("/register", methods=["GET", "POST"])
def register():
    form = accounts_form.RegisterForm()
    if not form.validate_on_submit():
        return render_template("/accounts/register.html", form=form)

    user = users.User()
    form.populate_obj(user)

    print(form.data)
    user.password = generate_password_hash(form.password.data, method="sha256")

    # db management
    models.db.session.add(user)
    models.db.session.commit()

    return redirect(url_for("accounts.login"))

@bp.route("/dashboard")
@login_required
def dashboard():
    folio_data = models.db.session.query(folios.Folio).all()
    return render_template("/accounts/dashboard.html", folio_data=folio_data)

