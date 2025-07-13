import pandas as pd
import joblib

def predict_next():
    model = joblib.load("models/model.pkl")
    df = pd.read_csv("data/processed/features.csv")
    
    df.dropna(inplace=True)

    # Use last row for prediction
    feature_cols = ["Close", "High", "Low", "Open", "Volume", "DayOfWeek"]
    if not all(col in df.columns for col in feature_cols):
        raise ValueError("Required feature columns are missing in features.csv")

    X = df[feature_cols].tail(1)

    # Predict
    prediction = model.predict(X)
    return prediction.tolist()
