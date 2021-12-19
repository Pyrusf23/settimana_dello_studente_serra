import os

class Production(object):
    SECRET_KEY=os.urandom(24)
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI="sqlite:///db.sqlite3"

class Debug(Production):
    DEBUG=True
    SEND_FILE_MAX_AGE_DEFAULT=0