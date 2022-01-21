from models.db import db

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()

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