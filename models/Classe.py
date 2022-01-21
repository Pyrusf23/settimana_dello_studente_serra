from models.db import db

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()

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