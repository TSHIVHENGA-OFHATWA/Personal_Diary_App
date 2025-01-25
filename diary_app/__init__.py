from flask import Flask
import os
from dotenv import load_dotenv
import secrets
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

load_dotenv()

conn = SQLAlchemy()
DB_NAME = "dairy.db"


def get_secret_key():
    """
    Retrieve or generate the application's SECRET_KEY
    if it doesn't exist in .env.

    The function first attempts to retrieve the SECRET_KEY from the .env file.
    If not found, it generates a new 32-byte random key, saves it to the .env
    file for future use, and returns it.

    Returns:
        str: The application's SECRET_KEY.
    """

    secret_key = os.getenv('SECRET_KEY')
    if not secret_key:
        secret_key = secrets.token_hex(32)  # Generate a secure random key
        with open('.env', 'a') as env_file:
            env_file.write(f"\nSECRET_KEY={secret_key}")
        print("SECRET_KEY has been generated and saved to .env")

    return secret_key


def create_app():
    """
    Create and configure the Flask application instance.

    This function sets up the Flask app, initializes the database connection,
    registers Blueprints for modularity, and configures Flask-Login.

    Returns:
        Flask: The configured Flask application instance.
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = get_secret_key()
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    conn.init_app(app)

    from .controllers import controllers
    from .authentication import authentication

    app.register_blueprint(controllers, url_prefix='/')
    app.register_blueprint(authentication, url_prefix='/')

    from .db_models import User, Diary

    with app.app_context():
        conn.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'authentication.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        """
        Load the user by their ID for Flask-Login.

        Args:
            id (int): The user ID.

        Returns:
            User: The user instance corresponding to the given ID.
        """
        return User.query.get(int(id))
    return app


def create_database(app):
    """
    Create the SQLite database if it doesn't already exist.

    Args:
        app (Flask): The Flask application instance.

    Workflow:
    1. Check if the database file exists in the specified path.
    2. If not, create the database using SQLAlchemy.
    """
    if not path.exists('diary_app/' + DB_NAME):
        conn.create_all(app=app)
        print('Database created!')
