from flask import Blueprint, render_template, request, flash, url_for, redirect
from .db_models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import conn
from flask_login import login_user, login_required, logout_user, current_user


""" Create a Blueprint for authentication-related routes """
authentication = Blueprint('authentication', __name__)


@authentication.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handles user registration.

    Methods:
    - GET: Render the registration page.
    - POST: Process the registration form and create a new user if valid.

    Workflow:
    1. Retrieve form data (email, full names, password, confirmPassword).
    2. Validate the data:
       - Ensure email is unique.
       - Ensure email and full names have valid lengths.
       - Ensure password and confirmPassword match.
       - Ensure password meets the length requirement.
    3. Hash the password using `generate_password_hash`.
    4. Create a new `User` object and save it to the database.
    5. Log the user in and redirect to the dashboard if registration is successful.

    Returns:
        Rendered HTML template for registration if GET or form validation fails.
        Redirect to the dashboard if registration is successful.
    """
    if request.method == 'POST':
        email = request.form.get('email')
        full_names = request.form.get('fullNames')
        password = request.form.get('password')
        confirmPassword = request.form.get('confirmPassword')
     
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 2:
            flash('Email must be greater than 2 characters.', category='error')
        elif len(full_names) < 2:
            flash('full names must be greater than 2 character.', category='error')
        elif password != confirmPassword:
            flash('Password don\'t match.', category='error')
        elif len(password) < 8:
            flash('Password must be at least 8 characters.', category='error')
        else:
            hashed_password=generate_password_hash(password, method='pbkdf2:sha256')
            new_user = User(email=email, full_names=full_names,
            password=hashed_password)
            conn.session.add(new_user)
            conn.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('controllers.dashboard'))

    return render_template("register.html", user=current_user)
 
@authentication.route('/login', methods=['GET', 'POST'])
def login():

   return render_template("login.html")


@authentication.route('/logout')
@login_required
def logout():
    
    logout_user()
    return render_template("dashboard.html")