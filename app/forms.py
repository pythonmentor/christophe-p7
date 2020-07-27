from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators


class Form(FlaskForm):
    message = StringField(
        "Posez votre question ici, par exemple Ou se trouve Clamart? Puis validez avec entrée",
        [validators.DataRequired()],
    )
    submit = SubmitField("Envoyer")
