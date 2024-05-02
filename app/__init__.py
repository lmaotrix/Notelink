from flask import Flask, flash, redirect, render_template, request, session, make_response
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


import controllers

controllers.posted
controllers.notes

if __name__ == "__main__":
    app.run()