import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# Training data
X = np.array([[1],[2],[3],[4],[5]])
y = np.array([40,50,65,75,90])

# Train model
model = LinearRegression()
model.fit(X,y)

st.title("📘 Study Hours vs Marks Predictor")

hours = st.number_input("Enter hours of study:", min_value=0.0, max_value=24.0, step=0.5)

if st.button("Predict Marks"):
    predicted_marks = model.predict([[hours]])
    st.success(f"If you study for {hours} hours, you may get **{predicted_marks[0]:.2f} marks** 🎯")

