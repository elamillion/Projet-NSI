from app import app
from flask import render_template
# routage 

@app.route("/")
def home():
    return render_template("register.html")
@app.route("/log")
def login_page():
    return render_template("log.html")