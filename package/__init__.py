from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import session
app = Flask(__name__)
app.config['SECRET_KEY']=['myscretkey']
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.db'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


db = SQLAlchemy(app)
from package import routes

