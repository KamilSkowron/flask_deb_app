from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_bcrypt import Bcrypt

# Start application
app = Flask(__name__)

# Configuration of the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 'Secret key' --> hide it later
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'

# Connect app with database
db = SQLAlchemy(app)

api = Api(app)

bcrypt = Bcrypt(app)

from deb import routes
from deb import restAPI