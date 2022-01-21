from models.db import db

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()

class Attivita(db.Model, Base):
    __tablename__ = "attivita"

    id = db.Column(db.Integer, primary_key=True)
    id_aula = db.Column(db.Integer, db.ForeignKey('aule.id'), nullable=False)
    nome = db.Column(db.String(80), nullable=False, unique=True)
    descrizione = db.Column(db.String(100), nullable=False)
    responsabile = db.Column(db.String(50), nullable=False)
    num_iscritti = db.Column(db.Integer, nullable=False, default=0)

    aula = relationship("Aula", back_populates="attivita")
    utenti_attivita_orari = relationship("conjUAO", back_populates="attivita")

    def __init__(self, id_aula, nome, descrizione, responsabile, num_iscritti):
        self.id_aula = id_aula
        self.nome = nome
        self.descrizione = descrizione
        self.responsabile = responsabile
        self.num_iscritti = num_iscritti
        