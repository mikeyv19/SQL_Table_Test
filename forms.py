from tokenize import String
from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    StringField,
    SubmitField,
    DecimalField,
    validators,
    TextAreaField,
)


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
    aisle = SelectField(
        "Shopping Aisle:",
        validators=[validators.InputRequired()],
        validate_choice=False,
    )
    submit1 = SubmitField("Submit Manual Item")


###########################
# INGREDIENT EDITING PAGE #
###########################
class CreateIngredient(FlaskForm):
    name = StringField("Name:", validators=[validators.InputRequired()])
    unit = SelectField(
        "Set Default Unit:",
        validators=[validators.InputRequired()],
        validate_choice=False,
    )
    protein = DecimalField("Protein:", validators=[validators.InputRequired()])
    carbs = DecimalField("Carbs:", validators=[validators.InputRequired()])
    fat = DecimalField("Fat:", validators=[validators.InputRequired()])
    fiber = DecimalField("Fiber:", validators=[validators.InputRequired()])
    sugar = DecimalField("Sugar:", validators=[validators.InputRequired()])
    item_unit_size = DecimalField(
        "Units per item:", validators=[validators.InputRequired()]
    )
    item_price = DecimalField("Store Price", validators=[validators.InputRequired()])
    aisle = SelectField(
        "Shopping Aisle:",
        validators=[validators.InputRequired()],
        validate_choice=False,
    )
    submit = SubmitField("Submit")


class AddUnitConversion(FlaskForm):
    unit2 = SelectField(
        "Unit Conversion Option:",
        validators=[validators.InputRequired()],
        validate_choice=False,
    )
    multiplyer = DecimalField(
        "How many base units?:", validators=[validators.InputRequired()]
    )
    submit2 = SubmitField("Submit")


#######################
# RECIPE EDITING PAGE #
#######################


class CreateRecipe(FlaskForm):
    recipe_name = StringField("Name", validators=[validators.DataRequired()])
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
    tags = StringField("Tags:")
    submit2 = SubmitField("Submit")


class AddIngredient(FlaskForm):
    name = SelectField(
        "Ingredient:",
        validators=[validators.InputRequired()],
        validate_choice=False,
    )
    unit = SelectField(
        "Unit Conversion Option:",
        validators=[validators.InputRequired()],
    )
    qty = DecimalField("Qty:", validators=[validators.InputRequired()])
    suffix = StringField("Notes")
    color1 = SelectField(
        "Color Tag:",
        choices=[
            ("default"),
            ("blue"),
            ("green"),
            ("light blue"),
            ("red"),
            ("yellow"),
            ("purple"),
            ("orange"),
            ("dark grey"),
            ("light grey"),
        ],
        validate_choice=False,
    )
    submit = SubmitField("Submit")


class AddInstruction(FlaskForm):
    instruction = TextAreaField(
        "Add Instruction Step:", validators=[validators.InputRequired()]
    )
    color2 = SelectField(
        "Color Tag:",
        choices=[
            ("default"),
            ("blue"),
            ("green"),
            ("light blue"),
            ("red"),
            ("yellow"),
            ("purple"),
            ("orange"),
            ("dark grey"),
            ("light grey"),
        ],
        validate_choice=False,
    )
    submit3 = SubmitField("Submit")


class SelectColor(FlaskForm):
    name = SelectField(
        "Color Tag:",
        choices=[
            ("default"),
            ("blue"),
            ("green"),
            ("light blue"),
            ("red"),
            ("yellow"),
            ("purple"),
            ("orange"),
            ("dark grey"),
            ("light grey"),
        ],
        validate_choice=False,
    )
    submit = SubmitField("Submit")


####################
# RECIPE VIEW PAGE #
####################
class RecipeMulti(FlaskForm):

    amount = DecimalField(
        "Recipe Multiplyer x:", validators=[validators.InputRequired()]
    )
    submit = SubmitField("Submit")


#####################
# UNIT EDITING PAGE #
#####################
class AddUnit(FlaskForm):
    unit = StringField(
        "Add Unit",
        validators=[validators.InputRequired()],
    )
    submit = SubmitField("Submit")


###########################
# WEEKLY DINNER PLAN PAGE #
###########################


class WeeklySelect(FlaskForm):
    rqty = DecimalField("Multiplyer", validators=[validators.InputRequired()])
    name = SelectField(
        "Recipe",
        validators=[validators.InputRequired()],
        validate_choice=False,
    )
    day = SelectField(
        "Color Tag:",
        choices=[
            ("Monday"),
            ("Tuesday"),
            ("Wednesday"),
            ("Thursday"),
            ("Friday"),
            ("Saturday"),
            ("Sunday"),
            ("Extra"),
        ],
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
