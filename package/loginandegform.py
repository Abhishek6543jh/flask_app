from flask_wtf import *
from wtforms import *

class registrationform(FlaskForm):
    username = StringField(label="Username")
    email = EmailField(label="email")
    password1=PasswordField(label="password")
    password2=PasswordField(label="password")
    submit = SubmitField(label="submit",id="submit")


class loginform(FlaskForm):
    username=StringField(label="username")
    password=PasswordField(label="password")
    login = SubmitField()