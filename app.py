from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Episode, Guest, Appearance

@app.route('/')
def index():
    return {
        "message": "Welcome to the Late Show API!"
    }
if __name__ == '__main__':
    app.run(debug=True)
