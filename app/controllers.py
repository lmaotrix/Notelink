from app import app
from flask import Flask, flash, redirect, render_template, request, session, make_response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/posted", methods=["GET", "POST"])
def posted():
    if request.method == "POST":
        note_title = request.form.get("Title")
        print("yes")

        if note_title:
            print("yes1")
            session["note_title"] = note_title
            print("yes2")
            return redirect("/notes")
        else:
            return render_template("index.html", error="Please add a title and a body to the note")
        
    return render_template("notes.html")

@app.route("/notes")
def notes():
    note_title = session.get("note_title", None)
    print("yes3")
    return render_template("notes.html", note_title=note_title)