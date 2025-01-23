from flask import Blueprint, render_template

text="this is test"
authentication = Blueprint('authentication', __name__)

@authentication.route('/register')
def register():
    return render_template("register.html")

@authentication.route('/login')
def login():
    return render_template("login.html", text="This is")

@authentication.route('/logout')
def logout():
    return render_template("dashboard.html")