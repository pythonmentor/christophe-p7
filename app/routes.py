from flask import render_template, flash, redirect
from app import my_app
from app.forms import Form


@my_app.route("/")
@my_app.route("/index")
def index():
    user = {"username": "chris"}
    return render_template("index.html", title="GrandPyBot", user=user)


@my_app.route("/message", methods=["GET", "POST"])
def message():
    form = Form()
    if form.validate_on_submit():
        flash("Clamart est une super ville")
        return redirect("/index")
    return render_template("form.html", title="message", form=form)
