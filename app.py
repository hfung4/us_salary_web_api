from flask import Flask, render_template, url_for, redirect, request
from utils.utils import get_percentile
from utils.predict import predict
from forms import UserInputForm
import numpy as np
from pathlib import Path
from strictyaml import load

app = Flask(__name__)

# read secret key
with open(Path("key", "key.yml"), "r") as key_file:
    key = load(key_file.read())

app.config["SECRET_KEY"] = key.data["SECRET_KEY"]


@app.route("/", methods=["GET", "POST"])
def user_form():
    form = UserInputForm()

    predicted_salary = 0

    # Get POST data
    if request.method == "POST":
        age_category = form.age_category.data
        industry = form.industry.data
        city_state = form.city_state.data
        overall_experience = form.overall_experience.data
        in_field_experience = form.in_field_experience.data
        education = form.education.data
        gender = form.gender.data
        race = form.race.data

        # TODO: create db with SQLAlchemy;
        # create "user" row with the above form data
        # Write data to User table

        # Get predictions from ML model
        prediction = predict(
            age_category=age_category,
            industry=industry,
            city_state=city_state,
            overall_experience=overall_experience,
            in_field_experience=in_field_experience,
            education=education,
            gender=gender,
            race=race,
        )
        predicted_salary = prediction[0]
        predicted_salary = float(predicted_salary)
        predicted_salary = round(predicted_salary, 2)
        print(predicted_salary)

        # Pass predicted_salary to results page
        return redirect(url_for("results", predicted_salary=predicted_salary))
    else:
        return render_template(
            "user_form.html", title="Input your information", form=form
        )


@app.route("/results/<float:predicted_salary>")
def results(predicted_salary):

    # Get the percentile
    percentile = get_percentile(predicted_salary)

    # Put results in a dictionary
    result_dict = {"predicted_salary": predicted_salary, "percentile": percentile}

    return render_template("results.html", title="Results", result=result_dict)


if __name__ == "__main__":
    app.run(debug=True)
