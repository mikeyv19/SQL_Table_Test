from flask_wtf import FlaskForm
from wtforms import SelectField, validators


class ReusableForm(FlaskForm):
    name = SelectField(
        "Enter a Name",
        validators=[validators.InputRequired()],
    )


# class ReusableForm(FlaskForm):
#     name = SelectField(
#         "Enter a Name",
#         choices=[("", "")] + [(uuid, name) for uuid, name in possible_names.items()],

#         validators=[validators.InputRequired()],
#     )

# possible_names = {"0": "hans","1": "sepp","3": "max",}  # options should be str so that empty choice option is valid


# class ReusableForm(FlaskForm):
#     name = SelectField(
#         "Enter a Name",
#         choices=[("", "")]
#         + [
#             (uuid, name) for uuid, name in possible_names.items()
#         ],  # [("", "")] is needed for a placeholder
#         validators=[validators.InputRequired()],
#     )
