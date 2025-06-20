git add config.py
git commit -m "Create config.py file with header comment"
import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    pass
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
