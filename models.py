from datetime import datetime
from database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    mobile = db.Column(db.String(20), nullable=False)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    paid_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    split_method = db.Column(db.String(50), nullable=False)  # equal, exact, percentage
    split_details = db.Column(db.JSON, nullable=False)  # JSON storing split details
    participants = db.Column(db.JSON, nullable=False)  # JSON storing user IDs
