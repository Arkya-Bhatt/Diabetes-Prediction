import streamlit as st
from model import load_model_and_scaler
from ui import sidebar_input_features
from eda import show_eda

st.set_page_config(
    page_title="Diabetes Prediction App",
    layout="wide",
    initial_sidebar_state="auto",
)

model, scaler = load_model_and_scaler()

if model is not None and scaler is not None:
    st.title("Diabetes Prediction App")
    st.markdown("""
    This application uses a Machine Learning model to predict the likelihood of an individual having diabetes. 
    Please enter the patient's data in the sidebar to get a prediction.
    """)

    # Get user input from the sidebar by calling the UI function
    user_input_df = sidebar_input_features()

    # Display the user's input data in the main area
    st.subheader("Patient's Input Data")
    st.dataframe(user_input_df)

    # Prediction button
    predict_button = st.sidebar.button("Predict")

    if predict_button:
        # Preprocess the user input
        scaled_user_input = scaler.transform(user_input_df)

        # Make prediction
        prediction = model.predict(scaled_user_input)
        prediction_proba = model.predict_proba(scaled_user_input)

        st.subheader("Prediction Result")
        
        # Display the result
        if prediction[0] == 1:
            st.error("The model predicts a HIGH risk of being Diabetic.")
            confidence = prediction_proba[0][1]
        else:
            st.success("The model predicts a LOW risk of being Diabetic.")
            confidence = prediction_proba[0][0]

        st.write(f"**Confidence:** {confidence*100:.2f}%")

    # --- EDA SECTION ---
    st.markdown("---")
    if st.checkbox("Show Exploratory Data Analysis (EDA)"):
        # Call the EDA function
        show_eda()
