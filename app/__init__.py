# Import flask and template operators
from flask import Flask

# Import SQLAlchemy
# from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Brave New World!'
