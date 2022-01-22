from models import db

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()

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
