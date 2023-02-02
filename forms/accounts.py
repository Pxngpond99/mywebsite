from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import validators


class LoginForm(FlaskForm):
    email = StringField(
        "name", validators=[validators.DataRequired(), validators.Length(min=3)]
    )
    password = StringField(
        "password",
        validators=[
            validators.DataRequired(),
            validators.Length(min=3, message="มากกว่า 3"),
        ],
    )


class RegisterForm(FlaskForm):
    email = StringField(
        "email", validators=[validators.DataRequired(), validators.Length(min=3)]
    )
    password = StringField(
        "password",
        validators=[
            validators.DataRequired(),
            validators.Length(min=3, message="มากกว่า 3"),
        ],
    )
    first_name = StringField("first_name", validators=[validators.DataRequired()])
    last_name = StringField("password", validators=[validators.DataRequired()])