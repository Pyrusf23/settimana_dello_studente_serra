from models.db import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()

class User(UserMixin, db.Model, Base):
    __tablename__ = "utenti"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False) # Password sha256(64)
    id_classe = db.Column(db.Integer, db.ForeignKey('classi.id'), nullable=False)

    classe = relationship("Classe", back_populates="utenti")
    utenti_attivita = relationship("ConjUA", back_populates="utente")

    def __init__(self, email, password, id_classe):
        self.email = email
        self.password = generate_password_hash(password)
        self.id_classe = id_classe

    def verifyPassword(self, pwd):
        return check_password_hash(self.password, pwd)
