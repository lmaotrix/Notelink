# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash

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
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)

class Note(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


# add routes
from flask import redirect, render_template, request, session, make_response, flash

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/posted", methods=["GET", "POST"])
def posted():
    if request.method == "POST":
        if not session.get("logged_in"):
            return redirect("/access")
        
        note_title = request.form.get("title")
        note_content = request.form.get("content")
        user_id = session.get("user_id")

        if note_title and note_content:
            new_note = Note(title=note_title, content=note_content, user_id=user_id)
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

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            session['logged_in'] = True
            session['username'] = username
            flash("Login successful!", "success")
            return redirect("/")
        else:
            flash("Invalid username or password", "error")
            return redirect("/login")
    
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        repeat_password = request.form.get("repeat_password")

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("User already exists", "error")
            return redirect("/register")
        
        if password != repeat_password:
            flash("Passwords don't match. Check for syntax errors", "error")
            return redirect("/register")
        
        password_hash = generate_password_hash(password)

        new_user = User(username=username, password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! Please log in.", "success")
        return redirect("/login")
    
    return render_template("signup.html")

@app.route("/logout", methods=["POST"])
def logout():
    session['logged_in'] = False
    session.pop('username', None)
    return redirect("/")

@app.route("/access")
def access():
    return render_template("userarea.html")

from app import app

if __name__ == "__main__":
    app.run(debug=True)