from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Length(min=6, max=80)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=20)])
    remember = BooleanField('Rimani collegato')