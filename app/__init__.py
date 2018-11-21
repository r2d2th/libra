from flask import Flask

# Import SQLAlchemy
# from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)


from app import routes