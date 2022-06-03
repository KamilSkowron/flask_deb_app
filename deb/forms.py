from flask_wtf import FlaskForm
from wtforms import PasswordField,EmailField,SubmitField,StringField, IntegerField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    email_address = EmailField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')



class DebForm(FlaskForm):
    borrower = StringField(label='Borrower', validators=[DataRequired()])
    description = StringField(label='description', validators=[DataRequired()])
    amount = IntegerField(label='Amount', validators=[DataRequired()])
    submit = SubmitField(label='Add Deb')

