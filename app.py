# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd
import pickle

# Load the model using binary mode 'rb'

loaded_model=pd.read_pickle(r'C:\Users\HP\Desktop\PORTFOLIO\banglore_home_prices_model.pickle')

# Create a function to predict the price
def predict_price(location, total_sqft, bath, bhk):
    input_data = pd.DataFrame({'location': [location],
                               'total_sqft': [total_sqft],
                               'bath': [bath],
                               'bhk': [bhk]})
    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit app
st.title("Bangalore Home Price Prediction")

# Input features
location = st.text_input("Location", "")
total_sqft = st.text_input("Total Square Feet", "")
bath = st.number_input("Bathrooms", 1, 10, 1)
bhk = st.number_input("BHK (Bedrooms)", 1, 10, 1)

# Predict and display the price
if st.button("Predict Price"):
    if location and total_sqft and bath and bhk:
        price = predict_price(location, total_sqft, bath, bhk)
        st.success(f"Predicted Price: {price:.2f} Lakhs")
    else:
        st.warning("Please fill in all the details.")

st.info("Enter the property details and click 'Predict Price'.")