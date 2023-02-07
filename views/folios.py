from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, login_user, logout_user

from werkzeug.security import generate_password_hash, check_password_hash

from forms import folios as folios_form
import models
from models import folios

bp = Blueprint("folios", __name__, url_prefix="/folios")


@bp.route("/create", methods=["GET", "POST"])
def create():
    form = folios_form.FolioForm()
    if not form.validate_on_submit():
        return render_template("/folios/create.html", form=form)

    folio = folios.Folio()
    form.populate_obj(folio)

    models.db.session.add(folio)
    models.db.session.commit()

    return redirect(url_for("accounts.dashboard"))


@bp.route("/<folio_id>/update", methods=["GET", "POST"])
def update(folio_id):
    folio = (
        models.db.session.query(folios.Folio)
        .filter_by(
            id=folio_id,
        )
        .first()
    )

    form = folios_form.FolioForm(obj=folio)
    if not form.validate_on_submit():
        return render_template("/folios/create.html", form=form)

    form.populate_obj(folio)

    # models.db.session.update(folio)
    models.db.session.commit()

    return redirect(url_for("accounts.dashboard"))


@bp.route("/<folio_id>/delete")
@login_required
def delete(folio_id):
    folio = (
        models.db.session.query(folios.Folio)
        .filter_by(
            id=folio_id,
        )
        .first()
    )

    models.db.session.delete(folio)
    models.db.session.commit()

    return redirect(url_for("accounts.dashboard"))


@bp.route("/<folio_id>")
@login_required
def view(folio_id):
    folio = (
        models.db.session.query(folios.Folio)
        .filter_by(
            id=folio_id,
        )
        .first()
    )

    return render_template("/folios/view.html", folio=folio)