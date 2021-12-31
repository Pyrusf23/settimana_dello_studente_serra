from models.db import db

class Orario(db.Model):
    __tablename__ = "orari"

    id = db.Column(db.Integer, primary_key=True)
    ora_giorno = db.Column(db.String(30), nullable=False, unique=True)

    def __init__(self, ora_giorno):
        self.ora_giorno = ora_giorno