from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import validators
from wtforms import widgets


class FolioForm(FlaskForm):
    email = StringField(
        "email", validators=[validators.DataRequired(), validators.Length(min=3)]
    )
    name = StringField("Name", validators=[validators.DataRequired()])
    biography = StringField("Biography", widget=widgets.TextArea())
    education = StringField("Education", widget=widgets.TextArea())
