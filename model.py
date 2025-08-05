import streamlit as st
import pickle

@st.cache_data
def load_model_and_scaler():
    try:
        with open('classification_model.pkl', 'rb') as model_file:
            model = pickle.load(model_file)
            
        with open('scaler.pkl', 'rb') as scaler_file:
            scaler = pickle.load(scaler_file)
            
        return model, scaler
    
    except Exception as e:
        st.error(f"Error loading model and scaler: {e}")
        return None, None