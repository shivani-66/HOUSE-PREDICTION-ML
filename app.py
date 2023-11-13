# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 21:10:34 2023

@author: HP
""" 

import numpy as np
import pickle
import pandas as pd
import streamlit as st
import json
import math


from PIL import Image

pickle_in = open("linear.pkl","rb")
linear=pickle.load(pickle_in)

        



with open("columns.json", 'r') as obj:
    __data_columns = json.load(obj)["Columns"]
    __locations = __data_columns[3:]

def welcome():
    return "Welcome All"




def predict_price(location,total_sqft,total_bath,BHK):
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError as e:
        loc_index = -1
    lis = np.zeros(len(__data_columns))
    lis[0] = total_sqft
    lis[1] = total_bath
    lis[2] = BHK 
    
    if loc_index >= 0:
        lis[loc_index] = 1
    price = round(linear.predict([lis])[0], 2)
    strp = ' lakhs'
    if math.log10(price) >= 2:
        price = price / 100
        price = round(price, 2)
        strp = " crores"
    return str(price) + strp


def main():
    st.title("HOUSE PRICE PREDICTION")
    html_temp="""
    <div style="background-color:red";padding:10px">
    <h2 style="color:black";text-align:center;">  House price prediction app </h2>
    </div>
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    location=st.selectbox("location",__locations)
    total_sqft=st.text_input("sqft")
    total_bath=st.text_input("bathrooms")
    BHK=st.text_input("BHK")
    
    result=""
    if st.button("predict"):
        result=predict_price(location,total_sqft, total_bath, BHK)
    st.success("Price of the House is {}".format(result))
    if st.button("about"):
        st.text("Thankyou!")
        st.text("built with streamlit")
if __name__=="__main__":
    main()
               