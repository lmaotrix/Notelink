from flask import Flask, flash, redirect, render_template, request, session, make_response
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SESSION_PERMANENT"] = False
app.config["SESSION.TYPE"] = "filesystem"
Session(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import controllers


#if __name__ == "__main__":
 #    eel.init("app/static")
  #   eel.start("index.html", size=(1000, 600), mode="chrome", port=8000, options={"chromeFlags": ["--start-fullscreen"]}, suppress_error=True)