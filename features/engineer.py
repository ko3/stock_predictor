# features/engineer.py

import pandas as pd
import os

def engineer_features(symbol="AAPL"):
    df = pd.read_csv(f"data/raw/{symbol}.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    df["DayOfWeek"] = df["Date"].dt.dayofweek
    df["Target"] = df["Close"].shift(-1)  # Predict next day's Close

    os.makedirs("data/processed", exist_ok=True)
    df.dropna().to_csv("data/processed/features.csv", index=False)
    print("Saved engineered features to data/processed/features.csv")

if __name__ == "__main__":
    engineer_features()
