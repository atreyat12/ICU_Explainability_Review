# streamlit_icu_los.py
import streamlit as st
import pandas as pd
import numpy as np
import xgboost as xgb
import joblib

def run_app():

# ---------------------------
# Load trained XGBoost model
# ---------------------------
    model = joblib.load("xgb_icu_los_model.pkl")  # your trained XGB model

# ---------------------------
# Streamlit App
# ---------------------------
    st.title("ICU Length of Stay Estimator")
    st.write("Enter patient information to estimate expected ICU Length of Stay (LOS). See how model prediction might or might not change with different demographics")

# ---------------------------
# User Inputs
# ---------------------------

# Numeric
    comorbidity_score = st.slider("Comorbidity Score", min_value=0, max_value=10, value=3)

    # Age group (one-hot)
    st.subheader("Age Group")
    age_group_options = [
        '10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-89','90+'
    ]
    age_group_selected = st.selectbox("Select Age Group", age_group_options)

    # Gender
    st.subheader("Gender")
    gender_selected = st.radio("Select Gender", ["M", "F"])

    # Insurance
    st.subheader("Insurance")
    insurance_selected = st.selectbox("Select Insurance", ["Medicare", "Private", "Other"])

    # Race
    st.subheader("Race / Ethnicity")
    race_options = [
        'ASIAN','BLACK','HISPANIC/LATINO','MULTIPLE RACE/ETHNICITY',
        'NATIVE HAWAIIAN/OTHER PACIFIC ISLANDER','OTHER','WHITE'
    ]
    race_selected = st.selectbox("Select Race", race_options)

    # Weekend admission
    is_weekend = st.checkbox("Admitted on Weekend?")

    # ---------------------------
    # Prepare input DataFrame
    # ---------------------------
    data = {
        'comorbidity_score': comorbidity_score,
        'is_weekend_1': int(is_weekend)
    }

    # One-hot encode age groups
    for ag in age_group_options:
        col = f"age_group_{ag}"
        data[col] = 1 if ag == age_group_selected else 0

    # One-hot encode gender
    data['gender_M'] = 1 if gender_selected == "M" else 0

    # One-hot encode insurance
    data['insurance_Medicare'] = 1 if insurance_selected == "Medicare" else 0
    data['insurance_Private'] = 1 if insurance_selected == "Private" else 0
    # Other insurance types will be 0 automatically

    # One-hot encode race
    for r in race_options:
        col = f"race_{r}"
        data[col] = 1 if r == race_selected else 0

    # Convert to DataFrame
    input_df = pd.DataFrame([data])

    # ---------------------------
    # Make Prediction
    # ---------------------------
    if st.button("Predict ICU LOS"):
        pred_log = model.predict(input_df.values)  # if trained on log(LOS)
        pred_los = np.exp(pred_log)               # convert back to days if needed
        
        st.success(f"Predicted ICU Length of Stay: {pred_los[0]:.1f} days")

if __name__ == "__main__":
    run_app()