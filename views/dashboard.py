from flask import Blueprint, render_template, redirect, url_for, request, flash
from forms.loginForm import LoginForm
from forms.registrazioneForm import RegistrazioneForm
from models import db, User, execute_query
from flask_login import login_user, current_user, logout_user, login_required


# Settings
dashboard = Blueprint('dashboard', __name__)

# Routing
@dashboard.route("/orario")
@login_required
def timetable():
    orario=[[0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]] # Chri mi spiace per l'ineleganza ma purtroppo dovevo necessariamente fare questa matrice perché sennò jinja impazziva
            # Questa matrice segue quest'ordine giorno[ora[placeholder]]
    giorni = {9:0, 10:1, 11:2, 14:3, 15:4, 16:5} # Dizionario che restituisce l'indice dei giorni della matrice in base al giorno del mese

    materie_query = """SELECT orari.giorno, orari.ora, materie.nome_materia
        FROM utenti, materie, orari, orari_materie_classi
        WHERE orari.id=orari_materie_classi.id_orario
            AND materie.id=orari_materie_classi.id_materia
            AND orari_materie_classi.id_classe=utenti.id_classe
            AND utenti.id=""" + "'" + str(current_user.id) + "'"
    materie_result = execute_query(materie_query).all() # Restituisce una tupla (giornoDelMese, ora, materia)
    # print(materie_result)
    for materia in materie_result:
        giorno = giorni[materia[0]] # Traduce il giorno del mese da query nell'indice appropriato per la matrice
        ora = (materia[1])-1 # Riduce di uno l'ora del giorno per renderlo appropriato alla matrice
        orario[giorno][ora] = materia[2]
    # print(orario)

    attivita_query = """SELECT orari.giorno, orari.ora, attivita.nome
        FROM utenti, orari, attivita, utenti_attivita, attivita_orari
        WHERE orari.id=attivita_orari.id_orario
            AND attivita.id=attivita_orari.id_attivita
            AND attivita_orari.id=utenti_attivita.id_attivita_orario
            AND utenti_attivita.id_utente=utenti.id
            AND utenti.id=""" + "'" + str(current_user.id) + "'"
    attivita_result = execute_query(attivita_query).all() # Restituisce una tupla (giornoDelMese, ora, attivita)
    # print(attivita_result)
    for attivita in attivita_result:
        giorno = giorni[attivita[0]]
        ora = (attivita[1])-1
        orario[giorno][ora] = attivita[2] # Sostituisce la materia dove c'è un'attività
    # print(orario)

    return render_template("orario.html", user=current_user.email, orario=orario)