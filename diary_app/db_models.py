from . import conn
from flask_login import UserMixin
from sqlalchemy.sql import func


class Diary(conn.Model):
    """
    Represents a diary entry in the database.

    Attributes:
        id (int): The unique identifier for the diary entry.
        info (str): The content of the diary entry.
        date (datetime): The timestamp when the diary entry was created.
                         Defaults to the current date and time.
        user_id (int): The ID of the user who created the diary entry,
                       referencing the `User` model.

    Relationships:
        - Belongs to a `User` via a foreign key.
    """
    id = conn.Column(conn.Integer, primary_key=True)
    info = conn.Column(conn.String(1000000000))
    date = conn.Column(conn.DateTime(timezone=True), default=func.now())
    user_id = conn.Column(conn.Integer, conn.ForeignKey('user.id'))


class User(conn.Model, UserMixin):
    """
    Represents a user in the database.

    Attributes:
        id (int): The unique identifier for the user.
        email (str): The user's email address. Must be unique.
        password (str): The user's hashed password.
        full_names (str): The user's full name.
        info_notes (list): A list of `Diary` entries associated with the user.

    Relationships:
        - Has a one-to-many relationship with `Diary`.
    """
    id = conn.Column(conn.Integer, primary_key=True)
    email = conn.Column(conn.String(150), unique=True)
    password = conn.Column(conn.String(150))
    full_names = conn.Column(conn.String(150))
    info_notes = conn.relationship('Diary')
