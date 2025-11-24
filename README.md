# Explainability in Healthcare
Applying explainability techniques to predictive modeling in healthcare. 

# 🏥 ICU Outcomes in MIMIC-IV: Mortality & LOS Analysis

This project investigates ICU outcomes using the **MIMIC-IV** dataset, focusing on **mortality** and **length of stay (LOS)**. We use descriptive statistics, visualizations, and predictive modeling with explainability to explore disparities by **race**, **insurance**, **gender**, and **clinical covariates**.

### 🤖To Run App
* `git clone` repo to pull files locally
* Run `streamlit run streamlit_run.py`

## 📁 Contents

* `XAI_ICU_Study.ipynb`: Full analysis in Jupyter Notebook
* `streamlit_run.py`: Streamlist App
* `requirements.txt`: Requirements to run model and app
* `xgb_icu_los_model.pkl`: Model trained to predict ICU length of stay outcomes

## 📊 Dataset

**MIMIC-IV (v2.2)** – A large, freely available database from ICU patients at Beth Israel Deaconess Medical Center (2008–2022).
Access requires [CITI training](https://about.citiprogram.org/) and [PhysioNet credentialing](https://physionet.org/).

Key Tables:

* `admissions.csv`
* `patients.csv`
* `icu_stays.csv`
* `diagnoses_icd.csv`

## 🔍 Objectives

* Explore how **race, gender, age, insurance type, and comorbidities** influence ICU outcomes to see if they may be salient enough to be important features for predictive modeling. 
* Identify **disparities** in model predictions for **in-ICU mortality** and **length of stay** 
* **Predict mortality risk** and analyze **feature importance** to see potential healthcare practice impacts

## 📈 Methods

### Statistical Models

In order to explore if there are maybe any demographic features that could bias the model or that we think might be important in the model decision output, we ran some statistical models first with the **Length of Stay** ICU outcome and **Mortality** outcome.


### Machine Learning

* **XGBoost** model trained on ICU features
* **SHAP values** used to interpret feature contributions to mortality predictions and LOS
* **ICE** used to interpret how features impact model prediction


## 📌 Key Findings

* **Comorbidity score** was the strongest predictor of mortality for the model
* Race and insurance had some importance for the model in predicting both outcomes, but it's important to note that the dataset was highly imbalanced with mainly white patients.
* Gender had **minimal impact** on mortality predictions
* Overall it's important to continuous apply explainability in high risk healthcare settings to ensure we have an understanding of how models are coming to their decisions as there can be real implications on healthcare outcomes and provider care.
  

