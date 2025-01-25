from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .db_models import Diary
from . import conn
import json

""" Create a Blueprint for the controllers """
controllers = Blueprint('controllers', __name__)


@controllers.route('/', methods=['GET', 'POST'])
@login_required
def dashboard():
    """
    Dashboard view function that handles displaying and saving diary entries.

    Methods:
    - GET: Render the dashboard page with user information.
    - POST: Save a new diary entry to the database.

    Returns:
        Rendered HTML template for the dashboard page.

    Workflow:
    - If the request method is POST:
        1. Retrieve the diary entry from the form using `request.form.get('note')`.
        2. Validate the diary entry (ensure it's not empty).
        3. If valid, save the new diary entry to the database.
        4. Flash a success message.
        5. If invalid, flash an error message.
    - Render the `dashboard.html` template with the current user's data.

    Raises:
        None
    """
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Entry is too short!', category='error') 
        else:
            new_diary = Diary(info=note, user_id=current_user.id)  #providing the schema for the note 
            conn.session.add(new_diary) #adding the note to the database 
            conn.session.commit()
            flash('Diary entry saved!', category='success')

    return render_template("dashboard.html", user=current_user)