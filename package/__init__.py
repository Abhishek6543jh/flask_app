from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY']=['myscretkey']
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.db'
app.config['SESSION_PERMANENT'] = True
db = SQLAlchemy(app)
from package import routes

