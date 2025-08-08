
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestRegressor


model = pickle.load(open('climate_model.pkl', 'rb'))
features = pickle.load(open('features.pkl', 'rb'))

# App layout
st.set_page_config(page_title="🌍 Climate Change Predictor", layout="centered")
st.title("🌡️ Climate Change Indicator Prediction")
st.markdown("""
This app predicts **climate indicators** such as *Engagement* or *CO2 level* based on environmental features.
Fill the form below to see predictions.
""")


user_input = {}
for col in features:
    user_input[col] = st.number_input(f"Enter value for {col}", step=0.1)


if st.button("Predict"): 
    input_df = pd.DataFrame([user_input])
    prediction = model.predict(input_df)[0]
    st.success(f"📈 Predicted Value: {prediction:.2f}")
    st.balloons()

st.markdown("---")
st.caption("Made with ❤️ for Climate Change Modeling")