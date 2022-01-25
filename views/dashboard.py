from flask import Blueprint, render_template, redirect, url_for, request, flash
from forms.loginForm import LoginForm
from forms.registrazioneForm import RegistrazioneForm
from models import db, User, execute_query
from flask_login import login_user, current_user, logout_user, login_required


# Settings
dashboard = Blueprint('dashboard', __name__)

# Routing
@dashboard.route("/attivita")
@login_required
def activities():
    materie_query = """SELECT orari.giorno, orari.ora, materie.nome_materia
    FROM utenti, materie, orari, orari_materie_classi
    WHERE orari.id=orari_materie_classi.id_orario
	AND materie.id=orari_materie_classi.id_materia
	AND orari_materie_classi.id_classe=utenti.id_classe
	AND utenti.id=""" + "'" + str(current_user.id) + "'"
    materie_result = execute_query(materie_query).all()
    # print(materie_result)
    materie=[[[], [], [], [], [], [], []], [[], [], [], [], [], [], []], [[], [], [], [], [], [], []], [[], [], [], [], [], [], []], [[], [], [], [], [], [], []], [[], [], [], [], [], [], []]]
    giorni = {9:0, 10:1, 11:2, 14:3, 15:4, 16:5}
    for materia in materie_result:
        giorno = giorni[materia[0]]
        ora = (materia[1])-1
        materie[giorno][ora] = materia[2]
    # print(materie)
    
    # attivita_query = "placeholder"
    # attivita_result = execute_query(attivita_query).all()


    return render_template("attivita.html", user=current_user.email, materie=materie)