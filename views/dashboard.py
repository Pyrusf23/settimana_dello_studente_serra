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

    attivitaXutenti_query = """SELECT orari.giorno, orari.ora, attivita.nome
        FROM utenti, orari, attivita, utenti_attivita, attivita_orari
        WHERE orari.id=attivita_orari.id_orario
            AND attivita.id=attivita_orari.id_attivita
            AND attivita_orari.id=utenti_attivita.id_attivita_orario
            AND utenti_attivita.id_utente=utenti.id
            AND utenti.id=""" + "'" + str(current_user.id) + "'"
    attivitaXutenti_result = execute_query(attivitaXutenti_query).all() # Restituisce una tupla (giornoDelMese, ora, attivita)
    # print(attivitaXutenti_result)
    for attivita in attivitaXutenti_result:
        giorno = giorni[attivita[0]]
        ora = (attivita[1])-1
        orario[giorno][ora] = attivita[2] # Sostituisce la materia dove c'è un'attività
    # print(orario)

    return render_template("orario.html", user=current_user.email, orario=orario)

@dashboard.route("/attivita", methods=('GET', 'POST'))
@login_required
def activities():
    orario=[[[], [], [], [], [], [], []],
            [[], [], [], [], [], [], []],
            [[], [], [], [], [], [], []],
            [[], [], [], [], [], [], []],
            [[], [], [], [], [], [], []],
            [[], [], [], [], [], [], []]] # Chri mi spiace per l'ineleganza ma purtroppo dovevo necessariamente fare questa matrice perché sennò jinja impazziva
            # Questa matrice segue quest'ordine giorno[ora[vettoreAttività[]]]
    giorni = {9:0, 10:1, 11:2, 14:3, 15:4, 16:5} # Dizionario che restituisce l'indice dei giorni della matrice in base al giorno del mese

    attivita_query = """SELECT orari.giorno, orari.ora, attivita.id AS id_attivita, attivita.nome, attivita.descrizione, attivita.responsabile, attivita.num_iscritti, aule.denominazione AS nome_lab, aule.num_posti AS num_posti_aula
        FROM orari, attivita_orari, attivita, aule, classi, utenti
        WHERE orari.id=attivita_orari.id_orario
            AND attivita_orari.id_attivita=attivita.id
            AND attivita.id_aula=aule.id
            AND aule.centrale_succursale=classi.centrale_succursale
            AND classi.id=utenti.id_classe
        	AND attivita.num_iscritti<num_posti_aula
            AND utenti.id=""" + "'" + str(current_user.id) + "'"
    attivita_result = execute_query(attivita_query).all() # Restituisce una tupla ([0]giornoDelMese,
                                                          #                        [1]ora,
                                                          #                        [2]id_attivita,
                                                          #                        [3]nome_attivita,
                                                          #                        [4]descrizione,
                                                          #                        [5]responsabile,
                                                          #                        [6]num_iscritti,
                                                          #                        [7]nome_lab,
                                                          #                        [8]num_posti)
    # print(attivita_result)
    for attivita in attivita_result:
        giorno = giorni[attivita[0]]
        ora = (attivita[1])-1
        orario[giorno][ora].append({
            "id_attivita" : attivita[2],
            "nome_attivita" : attivita[3],
            "descrizione" : attivita[4],
            "responsabile" : attivita[5],
            "num_iscritti" : attivita[6],
            "nome_lab" : attivita[7],
            "num_posti" : attivita[8]
        }) # Aggiunge l'attività al vettore
    # print(orario)

    return render_template("attivita.html", user=current_user.email, orario=orario)