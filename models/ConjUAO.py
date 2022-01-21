from models import db

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()

class ConjUAO(db.Model, Base):
    __tablename__ = "utenti_attivita_orari"

    id = db.Column(db.Integer, primary_key=True)
    id_utente = db.Column(db.Integer, db.ForeignKey('utenti.id'), nullable=False)
    id_attivita = db.Column(db.Integer, db.ForeignKey('attivita.id'), nullable=False)
    id_orario = db.Column(db.Integer, db.ForeignKey('orari.id'), nullable=False)

    utente = relationship("User", back_populates="utenti_attivita_orari")
    attivita = relationship("Attivita", back_populates="utenti_attivita_orari")
    orario = relationship("Orario", back_populates="utenti_attivita_orari")

    def __init__(self, id_utente, id_attivita, id_orario):
        self.id_utente = id_utente
        self.id_attivita = id_attivita
        self.id_orario = id_orario
