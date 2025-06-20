from extensions import db
from sqlalchemy.orm import validates
class Episode(db.Model):
    __tablename__ = 'episodes'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)

    appearances = db.relationship('Appearance', backref='episode', cascade='all, delete-orphan')

    # GET episodes
    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "number": self.number
        }

    # GET episodes id
    def to_dict_with_appearances(self):
        return {
            "id": self.id,
            "date": self.date,
            "number": self.number,
            "appearances": [appearance.to_dict_basic() for appearance in self.appearances]
        }


class Guest(db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String, nullable=False)

    appearances = db.relationship('Appearance', backref='guest', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "occupation": self.occupation
        }

class Appearance(db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)

    # POST appearances
    def to_dict(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "guest_id": self.guest_id,
            "episode_id": self.episode_id,
            "guest": self.guest.to_dict(),
            "episode": {
                "id": self.episode.id,
                "date": self.episode.date,
                "number": self.episode.number
            }
        }

    # Nested appearance
    def to_dict_basic(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "guest_id": self.guest_id,
            "episode_id": self.episode_id,
            "guest": self.guest.to_dict()
        }
