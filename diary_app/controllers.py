from flask import Blueprint

controllers = Blueprint('controllers', __name__)

@controllers.route('/')
def home():
    return '<h1>This is home page test</h1>'