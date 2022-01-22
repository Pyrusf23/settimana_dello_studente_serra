from models.db import db

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()

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