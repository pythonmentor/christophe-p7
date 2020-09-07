"""Module to manage the parsing of the input sentence."""
from flask import render_template
from app import my_app


@my_app.route("/")
@my_app.route("/index")
def index():
    user = ["christophe", "Marc"]
    return render_template("index.html", user=user)


def process():
    # return json unify
    pass
