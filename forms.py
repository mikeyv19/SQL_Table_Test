from tokenize import String
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, DecimalField, validators


class ShoppingForm(FlaskForm):
    aqty = DecimalField("Qty:", validators=[validators.InputRequired()])
    name = SelectField(
        "Search an Item:",
        validators=[validators.InputRequired()],
        validate_choice=False,
    )
    submit = SubmitField("Submit")


class ManualShoppingForm(FlaskForm):
    bqty = DecimalField("Qty:", validators=[validators.InputRequired()])
    item = StringField("Manually Add Item:", validators=[validators.DataRequired()])
    submit1 = SubmitField("Submit Manual Item")


class CreateIngredient(FlaskForm):
    name = StringField("Name:", validators=[validators.InputRequired()])
    unit = SelectField(
        "Unit:",
        validators=[validators.InputRequired()],
        validate_choice=False,
    )
    aisle = SelectField(
        "Shopping Aisle:",
        validators=[validators.InputRequired()],
        validate_choice=False,
    )
    submit = SubmitField("Submit")


class SelectRecipe(FlaskForm):
    rqty = DecimalField("Multiplyer", validators=[validators.InputRequired()])
    name = SelectField(
        "Recipe",
        validators=[validators.InputRequired()],
        validate_choice=False,
    )
    submit = SubmitField("Submit")
