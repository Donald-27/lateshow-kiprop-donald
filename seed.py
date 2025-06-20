from app import app, db
from models import Episode, Guest, Appearance

with app.app_context():
    pass
    db.drop_all()
    db.create_all()
