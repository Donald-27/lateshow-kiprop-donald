from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create the Flask application
app = Flask(__name__)

# Load configuration from config.py
app.config.from_object('config.Config')

# Initialize database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import models after db is defined (we'll define these later in models.py)
from models import Episode, Guest, Appearance

@app.route('/')
def index():
    return {
        "message": "Welcome to the Late Show API!"
    }

if __name__ == '__main__':
    app.run(debug=True)
