from flask import Flask

#def create_app():
app = Flask(__name__)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from settings import Debug
app.config.from_object(Debug)

from models import db
db.init_app(app)

from views.main import main
app.register_blueprint(main)

from views.authentication import auth
app.register_blueprint(auth)

from views.dashboard import dashboard
app.register_blueprint(dashboard)

from models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#return app
app.run()