from flask import Flask
from flask_login import LoginManager
from settings import Production
from models import db
from views.main import main
from views.authentication import auth
from views.dashboard import dashboard
from models import User

def create_app():

    #def create_app():
    app = Flask(__name__)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)


    app.config.from_object(Production)

    db.init_app(app)


    app.register_blueprint(main)


    app.register_blueprint(auth)


    app.register_blueprint(dashboard)


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    #return app
    return app