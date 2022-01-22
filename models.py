from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import *

db = SQLAlchemy()

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model, Base):
    __tablename__ = "utenti"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False) # Password sha256(64)
    id_classe = db.Column(db.Integer, db.ForeignKey('classi.id'), nullable=False)

    classe = relationship("Classe", back_populates="utenti")
    utenti_attivita = relationship("ConjUA", back_populates="utente")

    def __init__(self, email, password, id_classe):
        self.email = email
        self.password = generate_password_hash(password)
        self.id_classe = id_classe

    def verifyPassword(self, pwd):
        return check_password_hash(self.password, pwd)


class Classe(db.Model, Base):
    __tablename__ = "classi"

    id = db.Column(db.Integer, primary_key=True)
    classe_sezione = db.Column(db.String(40), nullable=False, unique=True)
    centrale_succursale = db.Column(db.Integer, nullable=False)

    utenti = relationship("User", back_populates="classe")
    orari_materie_classi = relationship("ConjOMC", back_populates="classe")

    def __init__(self, classe_sezione, centrale_succursale):
        self.classe_sezione = classe_sezione
        self.centrale_succursale = centrale_succursale


class Orario(db.Model, Base):
    __tablename__ = "orari"

    id = db.Column(db.Integer, primary_key=True)
    giorno = db.Column(db.Integer, nullable=False)
    ora = db.Column(db.Integer, nullable=False)

    orari_materie_classi = relationship("ConjOMC", back_populates="orario")
    attivita_orari = relationship("ConjAO", back_populates="orario")

    def __init__(self, giorno, ora):
        self.giorno = giorno
        self.ora = ora


class Materia(db.Model, Base):
    __tablename__ = "materie"

    id = db.Column(db.Integer, primary_key=True)
    nome_materia = db.Column(db.String(40), nullable=False, unique=True)
    
    orari_materie_classi = relationship("ConjOMC", back_populates="materia")

    def __init__(self, nome_materia):
        self.nome_materia = nome_materia


class Aula(db.Model, Base):
    __tablename__ = "aule"

    id = db.Column(db.Integer, primary_key=True)
    denominazione = db.Column(db.String(40), nullable=False, unique=True)
    num_posti = db.Column(db.Integer, nullable=False)
    centrale_succursale = db.Column(db.Integer, nullable=False)

    attivita = relationship("Attivita", back_populates="aula")

    def __init__(self, denominazione, num_posti, centrale_succursale):
        self.denominazione = denominazione
        self.num_posti = num_posti
        self.centrale_succursale = centrale_succursale


class Attivita(db.Model, Base):
    __tablename__ = "attivita"

    id = db.Column(db.Integer, primary_key=True)
    id_aula = db.Column(db.Integer, db.ForeignKey('aule.id'), nullable=False)
    nome = db.Column(db.String(80), nullable=False, unique=True)
    descrizione = db.Column(db.String(100), nullable=False)
    responsabile = db.Column(db.String(50), nullable=False)
    num_iscritti = db.Column(db.Integer, nullable=False, default=0)

    aula = relationship("Aula", back_populates="attivita")
    attivita_orari = relationship("ConjAO", back_populates="attivita")

    def __init__(self, id_aula, nome, descrizione, responsabile, num_iscritti):
        self.id_aula = id_aula
        self.nome = nome
        self.descrizione = descrizione
        self.responsabile = responsabile
        self.num_iscritti = num_iscritti


class ConjOMC(db.Model, Base):
    __tablename__ = "orari_materie_classi"

    id = db.Column(db.Integer, primary_key=True)
    id_orario = db.Column(db.Integer, db.ForeignKey('orari.id'), nullable=False)
    id_materia = db.Column(db.Integer, db.ForeignKey('materie.id'), nullable=False)
    id_classe = db.Column(db.Integer, db.ForeignKey('classi.id'), nullable=False)

    orario = relationship("Orario", back_populates="orari_materie_classi")
    materia = relationship("Materia", back_populates="orari_materie_classi")
    classe = relationship("Classe", back_populates="orari_materie_classi")

    def __init__(self, id_orario, id_materia, id_classe):
        self.id_orario = id_orario
        self.id_materia = id_materia
        self.id_classe = id_classe


class ConjAO(db.Model, Base):
    __tablename__ = "attivita_orari"

    id = db.Column(db.Integer, primary_key=True)
    id_attivita = db.Column(db.Integer, db.ForeignKey('attivita.id'), nullable=False)
    id_orario = db.Column(db.Integer, db.ForeignKey('orari.id'), nullable=False)

    attivita = relationship("Attivita", back_populates="attivita_orari")
    orario = relationship("Orario", back_populates="attivita_orari")
    utenti_attivita = relationship("ConjUA", back_populates="attivita_orario")

    def __init__(self, id_attivita, id_orario):
        self.id_attivita = id_attivita
        self.id_orario = id_orario


class ConjUA(db.Model, Base):
    __tablename__ = "utenti_attivita"

    id = db.Column(db.Integer, primary_key=True)
    id_utente = db.Column(db.Integer, db.ForeignKey('utenti.id'), nullable=False)
    id_attivita_orario = db.Column(db.Integer, db.ForeignKey('attivita_orari.id'), nullable=False)

    utente = relationship("User", back_populates="utenti_attivita")
    attivita_orario = relationship("ConjAO", back_populates="utenti_attivita")

    def __init__(self, id_utente, id_attivita):
        self.id_utente = id_utente
        self.id_attivita = id_attivita


