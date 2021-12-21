from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=6, max=16)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=20)])
    remember = BooleanField('Rimani collegato')