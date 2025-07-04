# risk_calc.py
import numpy as np
import pandas as pd
import pickle

def load_model():
    with open("models/diabetes_model.pkl", "rb") as f:
        return pickle.load(f)

def predict_risk(input_data: dict) -> float:
    model = load_model()

    # Create DataFrame with correct column names
    input_df = pd.DataFrame([input_data])

    probability = model.predict_proba(input_df)[0][1]
    return probability
