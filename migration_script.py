from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# Graffetta

app = Flask(__name__)

from settings import Debug
app.config.from_object(Debug)

from models import *
db.init_app(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()

####################
#                  #
#  Comandi         #
#  by De Nisi      #
#  la graffa       #
#                  #
####################

# Migrazione
# python migration_script.py db migrate

# Esportazione su db
# python migration_script.py db upgrade