from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint("accounts", __name__, url_prefix="/accounts")


@bp.route("/login")
def login():
    return render_template("/accounts/login.html")


@bp.route("/do-login", methods=["POST"])
def do_login():
    email = request.form.get("email")
    password = request.form.get("password")

    print("-->", email, password)
    print(request.form)

    if not (email == "admin@local" and password == "password"):
        return redirect(url_for("accounts.login", message="invalid login"))

    return render_template("/accounts/login-success.html")

@bp.route("/open_profile")
def open_profile():
    return render_template("/main/profile.html")
