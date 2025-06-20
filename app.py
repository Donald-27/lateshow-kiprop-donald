# app.py - Main Flask app for Late Show API

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from models import Episode, Guest, Appearance

@app.route('/')
def home():
    return {"message": "Welcome to the Late Show API!"}

# GET episodes
@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes]), 200

# GET episodes id
@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode_by_id(id):
    episode = Episode.query.get(id)
    if episode:
        return jsonify(episode.to_dict_with_appearances()), 200
    return jsonify({"error": "Episode not found"}), 404

# GET guests
@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests]), 200

# POST appearances
@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()

    try:
        new_appearance = Appearance(
            rating=data['rating'],
            guest_id=data['guest_id'],
            episode_id=data['episode_id']
        )

        db.session.add(new_appearance)
        db.session.commit()

        return jsonify(new_appearance.to_dict()), 201

    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400

if __name__ == '__main__':
    app.run(debug=True)
