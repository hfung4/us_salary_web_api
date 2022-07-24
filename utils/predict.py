import pandas as pd
from survey_analysis.predict import make_prediction


def predict(
    age_category: str,
    industry: str,
    city_state: str,
    overall_experience: str,
    in_field_experience: str,
    education: str,
    gender: str,
    race: str,
) -> float:

    # Put input data to a dictionary
    d_input_data = {
        "age_category": [age_category],
        "industry": [industry],
        "city_state": [city_state],
        "overall_experience": [overall_experience],
        "in_field_experience": [in_field_experience],
        "education": [education],
        "gender": [gender],
        "race": [race],
    }
    # convert data dictionary to a pd.DataFrame with 1 row
    df_input_data = pd.DataFrame.from_dict(d_input_data)

    # Use ML model to get predicted salary
    # result is a dictionary of predicted salary, error, and model version
    result = make_prediction(input_data=df_input_data, form_data=True)

    return result["predictions"]
