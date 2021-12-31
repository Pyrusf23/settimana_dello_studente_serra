from models.db import db

class Classe(db.Model):
    __tablename__ = "classi"

    id = db.Column(db.Integer, primary_key=True)
    classe_sezione = db.Column(db.String(40), nullable=False, unique=True)

    def __init__(self, classe_sezione):
        self.classe_sezione = classe_sezione