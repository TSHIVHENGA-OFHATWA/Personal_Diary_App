from flask import Blueprint, render_template

controllers = Blueprint('controllers', __name__)

@controllers.route('/')
def dashboard():
    return render_template("dashboard.html")