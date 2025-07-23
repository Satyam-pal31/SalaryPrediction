import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("💼 Salary Class Predictor")
st.write("Enter details to predict if income is >50K or <=50K")

# Input Fields
age = st.slider("Age", 18, 90, 30)
education_num = st.slider("Education Number", 1, 16, 10)
capital_gain = st.number_input("Capital Gain", 0, 100000, 0)
capital_loss = st.number_input("Capital Loss", 0, 10000, 0)
hours_per_week = st.slider("Hours per Week", 1, 100, 40)

gender = st.selectbox("Gender", ["Male", "Female"])
gender_code = 1 if gender == "Male" else 0  # or adjust based on your dataset

# Final input array
features = np.array([[age, education_num, capital_gain, capital_loss, hours_per_week, gender_code]])

# Predict
if st.button("Predict"):
    prediction = model.predict(features)
    if prediction[0] == 1:
        st.success("✅ Income > 50K")
    else:
        st.warning("❌ Income <= 50K")
