from fastapi import FastAPI
from models.predict import predict_next

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Stock Predictor running"}

@app.get("/predict")
def predict():
    result = predict_next()
    return {"prediction": result}
