from . import db



class Folio(db.Model):
    id = db.Column(
        db.BigInteger().with_variant(db.Integer, "sqlite"),
        primary_key=True,
        autoincrement=True,
    )

    name = db.Column(db.String)
    email = db.Column(db.String)

    biography = db.Column(db.String)
    education = db.Column(db.String)
    date_of_birth = db.Column(db.String)
