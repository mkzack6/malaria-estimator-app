# app.py
import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
model = joblib.load("model.pkl")
le_country = joblib.load("le_country.pkl")
le_region = joblib.load("le_region.pkl")

st.title("Malaria Case Estimator")

# User Inputs
country = st.selectbox("Select Country", le_country.classes_)
region = st.selectbox("Select WHO Region", le_region.classes_)
year = st.number_input("Year", min_value=2000, max_value=2030, value=2017)
deaths = st.number_input("Median No. of Deaths", min_value=0)

# Encode categorical features
country_encoded = le_country.transform([country])[0]
region_encoded = le_region.transform([region])[0]

# Predict
if st.button("Estimate Cases"):
    features = [[year, deaths, country_encoded, region_encoded]]
    prediction = model.predict(features)[0]
    st.success(f"Estimated median number of cases: {int(prediction):,}")
