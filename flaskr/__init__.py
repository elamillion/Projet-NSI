import os

from flask import Flask, json, render_template


# def create_app(test_config=None):
    # create and configure the app
app = Flask(__name__, static_folder="static")


@app.route("/")
def home():
    return render_template("register.html")

    # a simple page that says hello
@app.route('/hello')
def hello():
    return 'Hello, World!'

app.run()