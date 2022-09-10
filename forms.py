from tokenize import String
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, validators


class ShoppingForm(FlaskForm):
    name = SelectField(
        "Enter a Name",
        validators=[validators.InputRequired()],
    )
    SubmitField("Submit")


# class ShoppingForm(FlaskForm):
#     item = StringField("Item", validators=[DataRequired()])
#     submit = SubmitField("Submit")
