from models.db import db

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()

class Materia(db.Model, Base):
    __tablename__ = "materie"

    id = db.Column(db.Integer, primary_key=True)
    nome_materia = db.Column(db.String(40), nullable=False, unique=True)
    
    orari_materie_classi = relationship("ConjOMC", back_populates="materia")

    def __init__(self, nome_materia):
        self.nome_materia = nome_materia