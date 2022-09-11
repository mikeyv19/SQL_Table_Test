from tokenize import String
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, validators


class ShoppingForm(FlaskForm):
    name = SelectField(
        "Search an Item", validators=[validators.InputRequired()], validate_choice=False
    )
    submit = SubmitField("Submit")


class ManualShoppingForm(FlaskForm):
    item = StringField("Manually add Item:", validators=[validators.DataRequired()])
    submit1 = SubmitField("Submit Manual Item")
