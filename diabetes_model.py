# diabetes_model.py
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle

def train_and_save_model():
    df = pd.read_csv("data/diabetes.csv")

    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    with open("models/diabetes_model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("✅ Model trained and saved.")

if __name__ == "__main__":
    train_and_save_model()
