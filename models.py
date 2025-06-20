from app import db
class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
