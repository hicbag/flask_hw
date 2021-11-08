from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os 

basedir = os.path.abspath(os.path.dirname(__file__))

myapp = Flask(__name__)
myapp.config.from_mapping(
    SECRET_KEY='secret',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)
db = SQLAlchemy(myapp) 

from appp import routes, models

