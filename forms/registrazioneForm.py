from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length

class RegistrazioneForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Length(min=5, max=80)], render_kw={"placeholder": "Mail istituzionale"})
    password = PasswordField('Password', validators=[InputRequired(), Length(min=5, max=80)], render_kw={"placeholder": "Minimo 5 caratteri, massimo 80"})
    remember = BooleanField('Rimani collegato')