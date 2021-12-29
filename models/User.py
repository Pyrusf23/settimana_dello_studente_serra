from models.db import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False, unique=False) # Password sha256(64)

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)

    def verifyPassword(self, pwd):
        return check_password_hash(self.password, pwd)
