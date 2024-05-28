# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
Session(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# db models definitions
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)
    notes = db.relationship('Note', backref = 'user', lazy = True)

class Note(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


# add routes
from flask import redirect, render_template, request, session, make_response, flash

@app.route("/", methods=["GET", "POST"])
@app.route("/<int:note_id>", methods=["GET", "POST"])
def index(note_id=None):
    note = None
    if note_id:
        note = Note.query.filter_by(id=note_id, user_id=session.get("user_id")).first_or_404()

    if request.method == "POST":
        if not session.get("logged_in"):
            return redirect("/access")

        note_id = request.form.get("note_id")
        note_title = request.form.get("title")
        note_content = request.form.get("content")
        user_id = session.get("user_id")

        if note_id:
            note = Note.query.filter_by(id=note_id, user_id=user_id).first()
            if note:
                note.title = note_title
                note.content = note_content
        else:
            if note_title and note_content:
                note = Note(title=note_title, content=note_content, user_id=user_id)
                db.session.add(note)
            else:
                return render_template("index.html", note=note, error="Please add both a title and content to the note")
            
        db.session.commit()
        return redirect("/notes")
    
    return render_template("index.html", note=note)


@app.route("/notes", methods=["GET"])
def notes():
    if not session.get("logged_in"):
        return redirect("/access")
    
    
    user_id = session.get("user_id")
    notes = Note.query.filter_by(user_id=user_id).order_by(Note.id.desc()).all()
    return render_template("notes.html", notes=notes)

@app.route("/delete_note/<int:note_id>", methods=["POST"])
def delete_note(note_id):
    note = Note.query.filter_by(id=note_id, user_id=session.get("user_id")).first()
    if note:
        db.session.delete(note)
        db.session.commit()
        flash("Note deleted successfully")
    else:
        flash("Note not found")
    return redirect("/notes")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            session['logged_in'] = True
            session['username'] = username
            session['user_id'] = user.id
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