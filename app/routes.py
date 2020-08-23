from flask import render_template, flash, redirect
from app import my_app
from app.forms import Form


@my_app.route("/")
@my_app.route("/index")
def index():
    return render_template("index.html", title="GrandPyBot")

