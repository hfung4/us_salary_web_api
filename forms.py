from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
import json
from pathlib import Path

# Read JSON that contains levels of each input variable
with open(Path("utils", "artifacts", "col_levels.json")) as d:
    d_col_levels = json.load(d)  # automatically reads as a  python dictionary

# User input form


class UserInputForm(FlaskForm):
    # gender (3 selections)
    gender = SelectField("What is your gender?", choices=d_col_levels["gender"])

    # race (5 selections)
    race = SelectField("What is your race?", choices=d_col_levels["race"])

    # education (6 selections)
    education = SelectField(
        "What is your highest level of education?", choices=d_col_levels["education"]
    )
    # age (7 selections)
    age_category = SelectField(
        "What is your age?", choices=d_col_levels["age_category"]
    )
    # overall_experience (8 selections)
    overall_experience = SelectField(
        "How many years have you worked overall?",
        choices=d_col_levels["overall_experience"],
    )

    # in_field_experience (8 selections)
    in_field_experience = SelectField(
        "How many years have you worked in your current field?",
        choices=d_col_levels["in_field_experience"],
    )
    # city_state aka location (11 selections)
    city_state = SelectField(
        "Where is your current location?",
        choices=d_col_levels["city_state"],
    )
    # industry (11 selections)
    industry = SelectField(
        "Which industry do you work in?",
        choices=d_col_levels["industry"],
    )

    # submit
    submit = SubmitField("Submit")


if __name__ == "__main__":
    print(d_col_levels.keys())
    print(d_col_levels["education"])
