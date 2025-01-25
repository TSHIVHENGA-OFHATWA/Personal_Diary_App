from . import conn
from flask_login import UserMixin
from sqlalchemy.sql import func


class Diary(conn.Model):
    id = conn.Column(conn.Integer, primary_key=True)
    info = conn.Column(conn.String(1000000000))
    date = conn.Column(conn.DateTime(timezone=True), default=func.now())
    user_id = conn.Column(conn.Integer, conn.ForeignKey('user.id'))

class User(conn.Model, UserMixin):
    id = conn.Column(conn.Integer, primary_key=True)
    email = conn.Column(conn.String(150), unique=True)
    password = conn.Column(conn.String(150))
    full_names = conn.Column(conn.String(150))
    info_notes = conn.relationship('Diary')