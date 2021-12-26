from models.db import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False, unique=True) # Password sha256(64)

    def __init__(self, email, password):
        self.email = email
        self.password = password