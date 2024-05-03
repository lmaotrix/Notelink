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

# add routes
from flask import redirect, render_template, request, session, make_response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/posted", methods=["GET", "POST"])
def posted():
    if request.method == "POST":
        note_title = request.form.get("title")
        print("yes")

        if note_title:
            print("yes1")
            session["note_title"] = note_title
            print("yes2")
            return redirect("/notes")
        else:
            return render_template("index.html", error="Please add a title and a body to the note")
        
    return render_template("notes.html")

@app.route("/notes", methods=["GET", "POST"])
def notes():
    if request.method == "POST":
        note_title = session.get("note_title", None)
        print("yes3")
        return render_template("notes.html", note_title=note_title)
    return render_template("notes.html")


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