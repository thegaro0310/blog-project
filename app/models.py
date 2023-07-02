from app import db  # Import the SQLAlchemy instance from app.py
from datetime import datetime  # Import the datetime module

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    author = db.Column(db.String(50))
    views = db.Column(db.Integer, default=0)
    date = db.Column(db.DateTime, default=datetime.utcnow)
