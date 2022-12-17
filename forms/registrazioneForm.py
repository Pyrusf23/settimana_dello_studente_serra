from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField
from wtforms.validators import InputRequired, Length, regexp
from models import Classe

class RegistrazioneForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        all_class = Classe.query.with_entities(Classe.id, Classe.classe_sezione).all()
        self.class_id.choices = [
            (classe.id, classe.classe_sezione) for classe in all_class
        ]

    email = StringField('Email', validators=[InputRequired(), Length(min=5, max=80), regexp("^([A-Z]|[a-z]){1,}(\.([A-Z]|[a-z]){1,}){1,}$", flags=0, message="ERRORE: Email non valida")], render_kw={"placeholder": "Mail istituzionale"})
    password = PasswordField('Password', validators=[InputRequired(), Length(min=5, max=20)], render_kw={"placeholder": "Minimo 5 caratteri, massimo 20"})
    class_id = SelectField("Classe", coerce=int)
    remember = BooleanField('Rimani collegato')