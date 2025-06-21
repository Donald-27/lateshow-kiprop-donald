# lateshow-kiprop-donald


Lateshow Challenge – Flask REST API
This project is a mock code challenge called “Lateshow” where you build a REST API using Flask. The app lets you manage a fictional talk show that has episodes, guests, and guest appearances. It’s a great project to practice working with Flask, databases, and routing.

What This Project Does
The API lets users:

List all talk show episodes

Add new guests to the show

Assign a guest to appear in a specific episode

View and delete episodes

Seed and initialize a simple SQLite database

This is a backend-only application (there’s no frontend). You can test it using tools like Postman or curl.

Technologies Used
Python 3

Flask

Flask SQLAlchemy

Flask Migrate

SQLite

Flask CORS

How to Set Up the Project
Step 1: Clone the repository from GitHub
Use git clone <repo-link> and move into the project directory.

Step 2: Create and activate a virtual environment
Run python3 -m venv .venv to create the environment.
Activate it using source .venv/bin/activate if you're on Mac/Linux or .venv\Scripts\activate if you're on Windows.

Step 3: Install the required packages
Make sure you're in the root of the project and run pip install -r requirements.txt. If you don’t have a requirements.txt, you can install packages manually (Flask, Flask SQLAlchemy, Flask Migrate, Flask CORS) and then run pip freeze > requirements.txt to create one.

Step 4: Set up the database
In the root of the project, set the Flask app environment variable like this:
On Mac/Linux: export FLASK_APP=app.py
On Windows: set FLASK_APP=app.py

Then run the following commands to set up your database:

flask db init

flask db migrate -m "Initial migration"

flask db upgrade

Step 5: Seed the database
Run python seed.py to fill your database with some sample episodes, guests, and appearances.

Running the App
Once your database is ready and seeded, run the server using:

flask run

The app will be running on http://localhost:5000.

You can now visit your API using Postman or your browser. Some routes like /reviews will return JSON you can check.

Available Routes
GET /episodes will list all episodes

POST /episodes lets you add a new episode

GET /episodes/<id> shows details of one episode

DELETE /episodes/<id> deletes an episode

GET /guests lists all guests

POST /guests creates a new guest

POST /appearances connects a guest to an episode

Notes
All JSON responses come back formatted as dictionaries or lists

There’s basic validation: for example, a guest needs a name and occupation

Errors like missing episodes or invalid guest IDs return useful messages

You can reset the whole project by deleting the migrations folder and app.db, then repeating the setup steps

About This Project
This is a mock backend coding challenge designed to test and demonstrate your ability to work with Flask, routing, databases, and REST API concepts. You can build on top of this project by adding authentication, advanced filtering, or even deploying it to a service like Render or Railway.

