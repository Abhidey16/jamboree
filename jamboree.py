import streamlit as st
import pandas as pd
import pickle
import numpy as np

# lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

st.title("Chance of admission in abroad collage or University")

# I want to take 4 inputs from the user
# Fuel type, Vehical type, engine power, seats



col1, col2,col3 = st.columns(3)

with col1: 
    # use radio for fuel_type
    GRE_Score = st.slider("GRE Score", 250, 340,step=1)

with col2: 
    TOEFL_Score= st.slider("TOEFL Score", 90, 120,step=1)

with col3:
    University_Rating = st.selectbox("University Rating",[1,2,3,4,5])



col4, col5, col6, col7 = st.columns(4)

with col4:
    SOP = st.slider("Statement Of Purpose", 1.0, 5.0,step=0.5)

with col5:
    LOR = st.slider("Letter Of Recomendation", 1.0, 5.0,step=0.5)    
    
with col6:
    CGPA= int(st.text_input('Enter CGPA', "11"))

with col7:
    Research = st.radio("Research Paper", ["Yes","No"]) 
    
    
    
model = pickle.load(open("jambo.pkl", "rb"))

encode_dict={
    # "fuel_type": {"Diesel": 1, "Petrol": 2, "LPG": 3, "Electric": 4},
    # "Vehical": {"Manual": 1, "Automatic": 2},
    # "Company": {"MARUTI":1, 'HYUNDAI':2},
    "Research" :{"Yes":1,"No":0}
     }



def model_pred(GRE_Score, TOEFL_Score, University_Rating, SOP,LOR, CGPA, Research):
    # create a dataframe
    Research = encode_dict["Research"][Research]
    # fuel_type = encode_dict["fuel_type"][fuel_type]
    # make = encode_dict["Company"][make]


    data = [[GRE_Score, TOEFL_Score, University_Rating, SOP,LOR, CGPA, Research]]

    return np.round(model.predict(data)[0],2)


if st.button("Predict"):
    st.write(model_pred(GRE_Score, TOEFL_Score, University_Rating, SOP,LOR, CGPA, Research))
else:
    st.write("Click on Predict, once you're done with the data")




# pip freeze > requirements.txt
# pipreqs .
    