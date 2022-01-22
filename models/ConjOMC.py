from models.db import db

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()

# Per ora ho commentato in migration_script.py, poi domani vediamo. Per ora lasciamo così e andiamo a festeggiare capodanno 23:55 31/12/2021
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
        