from typing import Union

from fastapi import FastAPI, Query

from model.diagnostico import predict as model_predict


app = FastAPI()


@app.get("/predict")
@app.post("/predict")
def read_item(
    temperature: float = Query(..., description="Body temperature in Celsius"),
    heart_rate: int = Query(..., description="Heart rate in beats per minute"),
    blood_pressure: int = Query(..., description="Blood pressure in format 'systolic/diastolic'")
):

    result = model_predict(temperature, heart_rate, blood_pressure)

    return {"result": result}
