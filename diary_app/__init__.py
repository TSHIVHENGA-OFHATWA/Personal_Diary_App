from flask import Flask
import os
from dotenv import load_dotenv
import secrets

load_dotenv()

def get_secret_key():
    """Generate a SECRET_KEY if it doesn't exist in .env."""
    secret_key = os.getenv('SECRET_KEY')
    if not secret_key:
        secret_key = secrets.token_hex(32)  # Generate a secure random key
        with open('.env', 'a') as env_file:
            env_file.write(f"\nSECRET_KEY={secret_key}")
        print("SECRET_KEY has been generated and saved to .env")
    
    return secret_key

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = get_secret_key()

    from .controllers import controllers
    from .authentication import authentication

    app.register_blueprint(controllers,url_prefix='/')
    app.register_blueprint(authentication,url_prefix='/')

    return app