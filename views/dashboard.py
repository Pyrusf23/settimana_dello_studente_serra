from flask import Blueprint, render_template, redirect, url_for, request, flash, request
from forms.loginForm import LoginForm
from forms.registrazioneForm import RegistrazioneForm
from models import Attivita, Aula, ConjAO, ConjUA, db, User, execute_query
from flask_login import login_user, current_user, logout_user, login_required


# Settings
dashboard = Blueprint('dashboard', __name__)

# Routing
# @dashboard.route("/orario")
# @login_required
# def timetable():
#     unsubscribeActivity(request)
#     orario=[[0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0]] # Chri mi spiace per l'ineleganza ma purtroppo dovevo necessariamente fare questa matrice perché sennò jinja impazziva
#             # Questa matrice segue quest'ordine giorno[ora[placeholder]]
#     giorni = {9:0, 10:1, 11:2, 14:3, 15:4, 16:5} # Dizionario che restituisce l'indice dei giorni della matrice in base al giorno del mese

#     materie_query = """SELECT orari.giorno, orari.ora, materie.nome_materia
#         FROM utenti, materie, orari, orari_materie_classi
#         WHERE orari.id=orari_materie_classi.id_orario
#             AND materie.id=orari_materie_classi.id_materia
#             AND orari_materie_classi.id_classe=utenti.id_classe
#             AND utenti.id=""" + "'" + str(current_user.id) + "'"
#     materie_result = execute_query(materie_query).all() # Restituisce una tupla (giornoDelMese, ora, materia)
#     # print(materie_result)
#     for materia in materie_result:
#         giorno = giorni[materia[0]] # Traduce il giorno del mese da query nell'indice appropriato per la matrice
#         ora = (materia[1])-1 # Riduce di uno l'ora del giorno per renderlo appropriato alla matrice
#         orario[giorno][ora] = materia[2]
#     # print(orario)

#     attivitaXutenti_query = """SELECT orari.giorno, orari.ora, attivita_orari.id AS id_attivita, attivita.nome, attivita.descrizione, attivita.responsabile, attivita.num_iscritti, aule.denominazione AS nome_lab, aule.num_posti AS num_posti_aula
#         FROM orari, attivita, attivita_orari, utenti_attivita, utenti, aule
#         WHERE orari.id=attivita_orari.id_orario
#             AND aule.id=attivita.id_aula
#             AND attivita.id=attivita_orari.id_attivita
#             AND attivita_orari.id=utenti_attivita.id_attivita_orario
#             AND utenti_attivita.id_utente=utenti.id
#             AND utenti.id=""" + "'" + str(current_user.id) + "'"
#     attivitaXutenti_result = execute_query(attivitaXutenti_query).all() # Restituisce una tupla ([0]giornoDelMese,
#                                                                         #                        [1]ora,
#                                                                         #                        [2]id_attivita_orario,
#                                                                         #                        [3]nome_attivita,
#                                                                         #                        [4]descrizione,
#                                                                         #                        [5]responsabile,
#                                                                         #                        [6]num_iscritti,
#                                                                         #                        [7]nome_lab,
#                                                                         #                        [8]num_posti)
#     # print(attivitaXutenti_result)
#     for attivita in attivitaXutenti_result:
#         giorno = giorni[attivita[0]]
#         ora = (attivita[1])-1
#         orario[giorno][ora] = ({
#             "id_attivita" : attivita[2],
#             "nome_attivita" : attivita[3],
#             "descrizione" : attivita[4],
#             "responsabile" : attivita[5],
#             "num_iscritti" : attivita[6],
#             "nome_lab" : attivita[7],
#             "num_posti" : attivita[8]
#         }) # Sostituisce la materia dove c'è un'attività
#     # print(orario)

#     return render_template("orario.html", user=current_user.email, orario=orario)

@dashboard.route("/attivita", methods=('GET', 'POST'))
@login_required
def activities():
    subscribeActivity(request)
    unsubscribeActivity(request)
    orario=[[[], [], [], [], [], [], []],
            [[], [], [], [], [], [], []],
            [[], [], [], [], [], [], []],
            [[], [], [], [], [], [], []]] # Chri mi spiace per l'ineleganza ma purtroppo dovevo necessariamente fare questa matrice perché sennò jinja impazziva
            # Questa matrice segue quest'ordine giorno[ora[vettoreAttività[]]]
    giorni = {19:0, 20:1, 21:2, 22:3} # Dizionario che restituisce l'indice dei giorni della matrice in base al giorno del mese

    attivita_query = """SELECT orari.giorno, orari.ora, attivita_orari.id AS id_attivita, attivita.nome, attivita.descrizione, attivita.responsabile, attivita.num_iscritti, aule.denominazione AS nome_lab, aule.num_posti AS num_posti_aula
        FROM orari, attivita_orari, attivita, aule, classi, utenti
        WHERE orari.id=attivita_orari.id_orario
            AND attivita_orari.id_attivita=attivita.id
            AND attivita.id_aula=aule.id
            AND aule.centrale_succursale=classi.centrale_succursale
            AND classi.id=utenti.id_classe
            AND utenti.id=""" + "'" + str(current_user.id) + "'"
    attivita_result = execute_query(attivita_query).all() # Restituisce una tupla ([0]giornoDelMese,
                                                          #                        [1]ora,
                                                          #                        [2]id_attivita_orario,
                                                          #                        [3]nome_attivita,
                                                          #                        [4]descrizione,
                                                          #                        [5]responsabile,
                                                          #                        [6]num_iscritti,
                                                          #                        [7]nome_lab,
                                                          #                        [8]num_posti)
    # print(attivita_result)
    # Qui giaciono le query di merda di Pyer
    # AND attivita.num_iscritti<num_posti_aula

    attivitaXutenti_query = """SELECT orari.giorno, orari.ora, attivita_orari.id AS id_attivita, attivita.nome, attivita.descrizione, attivita.responsabile, attivita.num_iscritti, aule.denominazione AS nome_lab, aule.num_posti AS num_posti_aula
        FROM orari, attivita, attivita_orari, utenti_attivita, utenti, aule
        WHERE orari.id=attivita_orari.id_orario
            AND aule.id=attivita.id_aula
            AND attivita.id=attivita_orari.id_attivita
            AND attivita_orari.id=utenti_attivita.id_attivita_orario
            AND utenti_attivita.id_utente=utenti.id
            AND utenti.id=""" + "'" + str(current_user.id) + "'"
    attivitaXutenti_result = execute_query(attivitaXutenti_query).all() # Restituisce una tupla ([0]giornoDelMese,
                                                                        #                        [1]ora,
                                                                        #                        [2]id_attivita_orario,
                                                                        #                        [3]nome_attivita,
                                                                        #                        [4]descrizione,
                                                                        #                        [5]responsabile,
                                                                        #                        [6]num_iscritti,
                                                                        #                        [7]nome_lab,
                                                                        #                        [8]num_posti)
    # print(attivitaXutenti_result)
    for attivita in attivita_result:
        giorno = giorni[attivita[0]]
        ora = (attivita[1])-1

        subscribed = 0
        for utenti_attivita in attivitaXutenti_result:
            attId_attivita = (utenti_attivita[2])
            if attId_attivita == attivita[2]:
                subscribed = 1

        orario[giorno][ora].append({
            "id_attivita" : attivita[2],
            "nome_attivita" : attivita[3],
            "descrizione" : attivita[4],
            "responsabile" : attivita[5],
            "num_iscritti" : attivita[6],
            "nome_lab" : attivita[7],
            "num_posti" : attivita[8],
            "iscritto" : subscribed
        }) # Aggiunge l'attività al vettore
    # print(orario)

    return render_template("attivita.html", user=current_user.email, orario=orario)

# Il parametro request è il modulo request importato da flask, quindi richiama la funzione e passagli request
def unsubscribeActivity(request): # Big head dai il nome che preferisci alla funzione

    # request.arg ritorna un object che contiene tutti i metodi per prelevare gli argomenti della richiesta, qualsiasi essa sia (GET, POST, PUT, ecc...)
    args = request.args

    # Frontend devi richiamare di nuovo la page con javascript e devi passare i parametri get all'url
    # Per fare il redirect in JS e dare dei parametri get si usa window.location.replace(window.location.href + "?" + "actionType=delete" + "&" + "id_attivita=id che ti prendi dal modal");
    # print(args)
    if args.get('actionType') == "delete": # Il primo parametro actionType indica il tipo di azione, in questo caso delete
        # print(args.get('id_attivita'))
        id_attivita = args.get('id_attivita')
        if id_attivita:
            # print(id_attivita)
            try:
                id_utente_attivita = ConjUA.query.filter_by(id_utente=current_user.id, id_attivita_orario=id_attivita).first()
                # print(id_utente_attivita.id)
                query = ConjUA.query.get(id_utente_attivita.id)
                # print(query)

                # Controlla i commenti nella funzione subscribeActivity()
                decrease_iscritti = Attivita.query.filter_by(id=

                    ConjAO.query.filter_by(id=

                        ConjUA.query.filter_by(id=id_utente_attivita.id).first().id_attivita_orario

                    ).first().id_attivita

                ).update({Attivita.num_iscritti: Attivita.num_iscritti-1})

                db.session.delete(query)
                db.session.commit()

                # Qui fai la query delete con l'id passato dal parametro
                # La funzione va richimata all'inizio nella funzione view che ti serve
                # Finito!
            except:
                pass
                # print("error")

def subscribeActivity(request):
    args = request.args
    # print(args)
    if args.get('actionType') == "create": # Il primo parametro actionType indica il tipo di azione, in questo caso create
        # print(args.get('id_attivita'))
        id_attivita_orario = args.get('id_attivita') # Ricordo che nonostante si chiami id_attivita indica l'id_attivita_orario
        if id_attivita_orario: # Questa sarò complicata da spiegare, 01/02/2022, 01:23

            id_orario = ConjAO.query.filter_by(id=id_attivita_orario).first().id_orario # Prendo l'id_orario conoscendo l'id_attivita_orario a cui è collegato
            # print(id_orario)
            query = """SELECT utenti_attivita.id
                FROM attivita_orari, utenti_attivita, utenti
                WHERE attivita_orari.id=utenti_attivita.id_attivita_orario
                    AND utenti_attivita.id_utente=utenti.id
                    AND utenti.id='""" + str(current_user.id) + """'
                    AND attivita_orari.id_orario='""" + str(id_orario) + "'"
            id_utente_attivita = execute_query(query).all() # Prendo tutte le attivita a cui l'utente è iscritto con lo stesso id_orario della nostra attività
            # print(id_utente_attivita)
            if id_utente_attivita != []: # Se c'è un'attivita bisogna sostituirla altrimenti aggiungerla
                id_utente_attivita = id_utente_attivita[0][0] # Questo lo devo fare per forza perché la query restituisce una roba tipo [(id,)]

                # Ora cominciamo con la roba particolare, questa query parte dall'id_utente_attivita, si prende l'id attivita_orario,
                # passa alla tabella attivita_orari, si prende l'id_attivita, passa alla tabella attivita e si prende il numero di iscritti per poi diminuirlo di 1.
                # Non so se ci fosse un metodo più semplice ma non è adesso il momento di pensarci, semmai vediamo dopo.
                decrease_iscritti = Attivita.query.filter_by(id=

                    ConjAO.query.filter_by(id=

                        ConjUA.query.filter_by(id=id_utente_attivita).first().id_attivita_orario

                    ).first().id_attivita

                ).update({Attivita.num_iscritti: Attivita.num_iscritti-1})

                # Modifica il record utente_attivita cambiando l'id_attivita_orario
                newConjUA = ConjUA.query.filter_by(id=id_utente_attivita).update({ConjUA.id_attivita_orario: id_attivita_orario})

                # Stessa cosa di prima ma aumenta di 1 l'attività interessata
                increase_iscritti = Attivita.query.filter_by(id=

                    ConjAO.query.filter_by(id=

                        ConjUA.query.filter_by(id=id_utente_attivita).first().id_attivita_orario

                    ).first().id_attivita

                ).update({Attivita.num_iscritti: Attivita.num_iscritti+1})

                db.session.commit()

            else:

                num_posti_aula = Aula.query.filter_by(
                    id = Attivita.query.filter_by(
                        id = ConjAO.query.filter_by(
                            id = id_attivita_orario
                        ).first().id_attivita
                    ).first().id_aula
                ).first().num_posti

                num_iscritti = Attivita.query.filter_by(
                    id = ConjAO.query.filter_by(
                        id = id_attivita_orario
                    ).first().id_attivita
                ).first().num_iscritti

                if(num_iscritti < num_posti_aula):

                    # Sto per fare una cazzata
                    # Inizio cazzata 16/12/2022 20:34
                    
                    id_attivita = ConjAO.query.filter_by(id=id_attivita_orario).first().id_attivita # Prendo l'id_attivita conoscendo l'id_attivita_orario a cui è collegato

                    query_check_attivita = """SELECT utenti_attivita.id
                        FROM attivita_orari, utenti_attivita, utenti
                        WHERE attivita_orari.id=utenti_attivita.id_attivita_orario
                            AND utenti_attivita.id_utente=utenti.id
                            AND utenti.id='""" + str(current_user.id) + """'
                            AND attivita_orari.id_attivita='""" + str(id_attivita) + "'"
                    id_attivita = execute_query(query_check_attivita).all() # Prendo tutte le attivita a cui l'utente è iscritto con lo stesso id_attivita della nostra attività
                    print(id_attivita)
                    if id_attivita == []:

                        # "Fine" cazzata 16/12/2022 21:14
                        

                        # Aggiunge il nuovo record
                        newConjUA = ConjUA(id_utente=current_user.id, id_attivita_orario=id_attivita_orario)
                        db.session.add(newConjUA)
                        db.session.commit() # Devo per forza committare perché non so se esiste una funzione per prendersi l'ultimo record aggiunto

                        id_utente_attivita = execute_query(query).first()[0] # Rifaccio la query di prima perché adesso ci sarà un record in db

                        # Aumento di uno il numero di iscritti all'attività interessata
                        increase_iscritti = Attivita.query.filter_by(id=

                            ConjAO.query.filter_by(id=

                                ConjUA.query.filter_by(id=id_utente_attivita).first().id_attivita_orario

                            ).first().id_attivita

                        ).update({Attivita.num_iscritti: Attivita.num_iscritti+1})

                        db.session.commit() # Committo gli update
                        # execute_query("INSERT INTO utenti_attivita (id_utente, id_attivita_orario) VALUES (" + str(current_user.id) + "," + id_attivita + ")")
                        # Qui fai la query create con l'id passato dal parametro
                        # La funzione va richimata all'inizio nella funzione view che ti serve
                        # Finito!
                    else:
                        # L'utente è già iscritto a questa attività
                        flash("Sei già iscritto a questa attività")

                else:
                    # L'attività è al completo
                    flash("I posti sono terminati")