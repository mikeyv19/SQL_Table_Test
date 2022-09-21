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


class CreateRecipe(FlaskForm):
    name = StringField("Name", validators=[validators.DataRequired()])
    course = SelectField(
        "Course",
        choices=[
            ("Entree"),
            ("Appetizer"),
            ("Dessert"),
            ("Side Dish"),
            ("Beverage"),
            ("Other"),
        ],
        validators=[validators.DataRequired()],
    )
    servings = DecimalField("Servings:", validators=[validators.InputRequired()])
    serving_size = StringField("Serving Size", validators=[validators.DataRequired()])
    submit = SubmitField("Submit")


class AddIngredient(FlaskForm):
    name = SelectField(
        "Ingredient:",
        validators=[validators.InputRequired()],
        validate_choice=False,
    )
    qty = DecimalField("Qty:", validators=[validators.InputRequired()])
    suffix = StringField("Notes")
    submit = SubmitField("Submit")


###########################
# WEEKLY DINNER PLAN PAGE #
###########################


class SelectRecipe(FlaskForm):
    rqty = DecimalField("Multiplyer", validators=[validators.InputRequired()])
    name = SelectField(
        "Recipe",
        validators=[validators.InputRequired()],
        validate_choice=False,
    )
    submit = SubmitField("Submit")


class SelectRecipe2(FlaskForm):
    rqty2 = DecimalField("Multiplyer", validators=[validators.InputRequired()])
    name2 = SelectField(
        "Recipe",
        validators=[validators.InputRequired()],
        validate_choice=False,
    )
    submit2 = SubmitField("Submit")


class SelectRecipe3(FlaskForm):
    rqty3 = DecimalField("Multiplyer", validators=[validators.InputRequired()])
    name3 = SelectField(
        "Recipe",
        validators=[validators.InputRequired()],
        validate_choice=False,
    )
    submit3 = SubmitField("Submit")


class SelectRecipe4(FlaskForm):
    rqty4 = DecimalField("Multiplyer", validators=[validators.InputRequired()])
    name4 = SelectField(
        "Recipe",
        validators=[validators.InputRequired()],
        validate_choice=False,
    )
    submit4 = SubmitField("Submit")


class SelectRecipe5(FlaskForm):
    rqty5 = DecimalField("Multiplyer", validators=[validators.InputRequired()])
    name5 = SelectField(
        "Recipe",
        validators=[validators.InputRequired()],
        validate_choice=False,
    )
    submit5 = SubmitField("Submit")


class SelectRecipe6(FlaskForm):
    rqty6 = DecimalField("Multiplyer", validators=[validators.InputRequired()])
    name6 = SelectField(
        "Recipe",
        validators=[validators.InputRequired()],
        validate_choice=False,
    )
    submit6 = SubmitField("Submit")


class SelectRecipe7(FlaskForm):
    rqty7 = DecimalField("Multiplyer", validators=[validators.InputRequired()])
    name7 = SelectField(
        "Recipe",
        validators=[validators.InputRequired()],
        validate_choice=False,
    )
    submit7 = SubmitField("Submit")
