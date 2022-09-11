from tokenize import String
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, validators


class ShoppingForm(FlaskForm):
    name = SelectField(
        "Select Item", validators=[validators.InputRequired()], validate_choice=False
    )
    SubmitField("Submit")


# class ShoppingForm(FlaskForm):
#     item = StringField("Item", validators=[DataRequired()])
#     submit = SubmitField("Submit")
