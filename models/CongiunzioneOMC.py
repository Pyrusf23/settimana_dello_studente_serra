from models import db

# Per ora ho commentato in migration_script.py, poi domani vediamo. Per ora lasciamo così e andiamo a festeggiare capodanno 23:55 31/12/2021
class ConjOMC(db.Model):
    __tablename__ = "orari_materie_classi"

    id = db.Column(db.Integer, primary_key=True)
    id_orario = db.Column(db.Integer, nullable=False, unique=False)
    id_materia = db.Column(db.Integer, nullable=False, unique=False)
    id_classe = db.Column(db.Integer, nullable=False, unique=False)

    def __init__(self, id_orario, id_materia, id_classe):
        self.id_orario = id_orario
        self.id_materia = id_materia
        self.id_classe = id_classe
        