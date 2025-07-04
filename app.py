# app.py
import streamlit as st
from risk_calc import predict_risk

st.set_page_config(page_title="Health Risk Tool", layout="centered")

st.title("🩺 Diabetes Risk Assessment Tool")

with st.form("risk_form"):
    st.subheader("Enter your details:")

    Pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, step=1)
    Glucose = st.slider("Glucose Level", 50, 200, 100)
    BloodPressure = st.slider("Blood Pressure", 40, 140, 80)
    SkinThickness = st.slider("Skin Thickness", 0, 100, 20)
    Insulin = st.slider("Insulin Level", 0, 900, 80)
    BMI = st.number_input("BMI", min_value=10.0, max_value=70.0, step=0.1)
    DPF = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, step=0.01)
    Age = st.slider("Age", 10, 100, 25)

    submit = st.form_submit_button("Calculate Risk")

if submit:
    input_data = {
        "Pregnancies": Pregnancies,
        "Glucose": Glucose,
        "BloodPressure": BloodPressure,
        "SkinThickness": SkinThickness,
        "Insulin": Insulin,
        "BMI": BMI,
        "DiabetesPedigreeFunction": DPF,
        "Age": Age
    }

    risk = predict_risk(input_data)
    st.success(f"🧠 Predicted Risk of Diabetes: **{risk * 100:.2f}%**")

    if risk > 0.5:
        st.warning("⚠️ High Risk. Please consult a healthcare provider.")
    else:
        st.info("✅ Low Risk. Keep maintaining a healthy lifestyle.")
