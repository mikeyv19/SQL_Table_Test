from tokenize import String
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, DecimalField, validators


class ShoppingForm(FlaskForm):
    aqty = DecimalField("Qty:", validators=[validators.InputRequired()])
    name = SelectField(
        "Search an Item", validators=[validators.InputRequired()], validate_choice=False
    )
    submit = SubmitField("Submit")


class ManualShoppingForm(FlaskForm):
    bqty = DecimalField("Qty:", validators=[validators.InputRequired()])
    item = StringField("Manually add Item:", validators=[validators.DataRequired()])
    submit1 = SubmitField("Submit Manual Item")
