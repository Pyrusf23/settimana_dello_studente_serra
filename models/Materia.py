from models.db import db

class Materia(db.Model):
    __tablename__ = "materie"

    id = db.Column(db.Integer, primary_key=True)
    nome_materia = db.Column(db.String(40), nullable=False, unique=True)

    def __init__(self, nome_materia):
        self.nome_materia = nome_materia