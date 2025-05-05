import os
import sqlite3
from flask import Flask, json, render_template


# def create_app(test_config=None):
    # create and configure the app
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("register.html")
@app.route("/log")
def login_page():
    return render_template("log.html")

app.run(debug=True)