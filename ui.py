import streamlit as st
import pandas as pd

def sidebar_input_features():
    st.sidebar.header("Patient Data")
    
    pregnancies = st.sidebar.slider('Pregnancies', 0, 17, 3, help="Number of times pregnant")
    glucose = st.sidebar.slider('Glucose', 40, 200, 120, help="Plasma glucose concentration a 2 hours in an oral glucose tolerance test")
    blood_pressure = st.sidebar.slider('Blood Pressure (mm Hg)', 20, 130, 72, help="Diastolic blood pressure")
    skin_thickness = st.sidebar.slider('Skin Thickness (mm)', 5, 100, 29, help="Triceps skin fold thickness")
    insulin = st.sidebar.slider('Insulin (mu U/ml)', 10, 900, 79, help="2-Hour serum insulin")
    bmi = st.sidebar.slider('BMI', 15.0, 70.0, 32.0, help="Body mass index (weight in kg / (height in m)^2)")
    dpf = st.sidebar.slider('Diabetes Pedigree Function', 0.07, 2.5, 0.47, help="A function that scores likelihood of diabetes based on family history")
    age = st.sidebar.slider('Age (years)', 21, 85, 33)
    
    user_data = {
        "Pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": blood_pressure,
        "SkinThickness": skin_thickness,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": dpf,
        "Age": age
    }
    
    features_df = pd.DataFrame(user_data, index=[0])
    return features_df