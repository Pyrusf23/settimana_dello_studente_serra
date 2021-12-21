from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length, regexp

class RegistrazioneForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Length(min=6, max=80), regexp("([A-Z]{1,}|[a-z]{1,})\.([A-Z]{1,}|[a-z]{1,})@isisserra\.edu\.it", flags=0, message="ERRORE: Email non valida")])
    username = StringField('Username', validators=[InputRequired(), Length(min=6, max=16)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=20)])
    remember = BooleanField('Rimani collegato')