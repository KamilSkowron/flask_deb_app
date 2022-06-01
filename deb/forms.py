from flask_wtf import FlaskForm
from wtforms import PasswordField,EmailField,SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')