from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, login_user, logout_user
from forms import accounts as accounts_form
import models
from models import users, folios

from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint("accounts", __name__, url_prefix="/accounts")


@bp.route("/login")
def login():
    return render_template("/accounts/login.html")

# @bp.route("/test")
# def test():
#     return render_template("/accounts/test.html")

@bp.route("/do-login", methods=["POST"])
def do_login():
    email = request.form.get("email")
    password = request.form.get("password")

    print("-->", email, password)
    print(request.form)

    if not (email == "admin@local" and password == "password"):
        return redirect(url_for("accounts.login", message="Invalid Login"))

    return render_template("/accounts/login-success.html")

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
