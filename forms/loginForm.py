from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField
from wtforms.validators import InputRequired, Length
from models import Classe

class LoginForm(FlaskForm):

    email = StringField('Email', validators=[InputRequired(), Length(min=6, max=80)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=20)])
    remember = BooleanField('Rimani collegato')