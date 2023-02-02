from flask_login import UserMixin
from . import db


class User(db.Model, UserMixin):
    id = db.Column(
        db.BigInteger().with_variant(db.Integer, "sqlite"),
        primary_key=True,
        autoincrement=True,
    )
    password = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)

    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
