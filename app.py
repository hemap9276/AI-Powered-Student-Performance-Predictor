import streamlit as st
import pickle

# Load trained model
with open("student_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page title
st.title("🎓 AI-Powered Student Performance Predictor")

st.write(
    "Enter the student's details below to predict the expected final score."
)

# User inputs
hours = st.number_input(
    "Hours Studied",
    min_value=0.0,
    max_value=24.0,
    value=5.0
)

previous_score = st.number_input(
    "Previous Exam Score",
    min_value=0.0,
    max_value=100.0,
    value=50.0
)

attendance = st.number_input(
    "Attendance Percentage",
    min_value=0.0,
    max_value=100.0,
    value=75.0
)

# Prediction button
if st.button("Predict Performance"):

    # Make prediction
    prediction = model.predict(
        [[hours, previous_score, attendance]]
    )[0]

    prediction = max(0, min(100, prediction))

    st.success(
        f"Predicted Final Score: {prediction:.2f}%"
    )

    # Performance message
    if prediction >= 75:
        st.balloons()
        st.write("🌟 Excellent performance!")

    elif prediction >= 50:
        st.write("👍 Good performance. Keep improving!")

    else:
        st.write("📚 More practice and study time may help.")
