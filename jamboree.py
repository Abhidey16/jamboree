import streamlit as st
import pandas as pd
import pickle
import numpy as np

st.title("Chance of admission in abroad collage or University")


col1, col2,col3 = st.columns(3)

with col1: 

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
    CGPA= st.slider("CGPA", 5.0, 10.0,step=0.01)

with col7:
    Research = st.radio("Research Paper", ["Yes","No"]) 
    
    
    
model = pickle.load(open("jambo.pkl", "rb"))

encode_dict={
    "Research" :{"Yes":1,"No":0}
     }



def model_pred(GRE_Score, TOEFL_Score, University_Rating, SOP,LOR, CGPA, Research):

    Research = encode_dict["Research"][Research]

    data = [[GRE_Score, TOEFL_Score, University_Rating, SOP,LOR, CGPA, Research]]

    return np.round(model.predict(data)[0],2)


if st.button("Predict"):
    st.write(model_pred(GRE_Score, TOEFL_Score, University_Rating, SOP,LOR, CGPA, Research))
else:
    st.write("Click on Predict, once you're done with the data")


