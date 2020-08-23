from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, validators


class Form(FlaskForm):
    message = TextAreaField("Votre message")
    submit = SubmitField("Envoyer")
