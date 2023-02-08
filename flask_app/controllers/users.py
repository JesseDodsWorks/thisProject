
from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


#######################################################
#                 loading start
#######################################################
@app.route("/")
def register_login():
    return render_template ("home.html")
#######################################################
