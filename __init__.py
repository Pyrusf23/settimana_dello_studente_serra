from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

from settings import Debug
app.config.from_object(Debug)

app.run()