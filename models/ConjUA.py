from models.db import db

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()

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
