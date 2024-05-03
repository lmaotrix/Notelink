# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# db models definitions
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    hash = db.Column(db.String(100), nullable=False)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


# add routes
from flask import redirect, render_template, request, session, make_response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/posted", methods=["GET", "POST"])
def posted():
    if request.method == "POST":
        if not session.get["logged_in"]:
            return render_template("401.html", message="ERROR: 401 unauthorized. You must be logged in to save notes")
        
        note_title = request.form.get("title")
        note_content = request.form.get("content")

        if note_title and note_content:
            new_note = Note(title=note_title, content=note_content)
            db.session.add(new_note)
            db.session.commit()
            return redirect("/notes")
        else:
            return render_template("index.html", error="Please add both a title and content to the note")
        
    return render_template("index.html")

@app.route("/notes", methods=["GET", "POST"])
def notes():
    notes = Note.query.all()
    return render_template("notes.html", notes=notes)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

from app import app

if __name__ == "__main__":
    app.run(debug=True)