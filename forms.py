from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ShoppingForm(FlaskForm):
    item = StringField("Item", validators=[DataRequired()])
    submit = SubmitField("Submit")
