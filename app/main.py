from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Cargar modelo entrenado
model = joblib.load("penguins_species_model.pkl")

class PenguinInput(BaseModel):
    culmen_length_mm: float
    culmen_depth_mm: float
    flipper_length_mm: float
    body_mass_g: float
    delta_15_n: float
    delta_13_c: float
    island: str
    sex: str
    clutch_completion: str

@app.get("/")
def home():
    return {"mensaje": "API clasificación Penguins 🐧"}

@app.post("/predict")
def predict(data: PenguinInput):

    # Crear DataFrame
    df = pd.DataFrame([{
        "Culmen Length (mm)": data.culmen_length_mm,
        "Culmen Depth (mm)": data.culmen_depth_mm,
        "Flipper Length (mm)": data.flipper_length_mm,
        "Body Mass (g)": data.body_mass_g,
        "Delta 15 N (o/oo)": data.delta_15_n,
        "Delta 13 C (o/oo)": data.delta_13_c,
        "Island": data.island,
        "Sex": data.sex,
        "Clutch Completion": data.clutch_completion
    }])

    # Crear feature engineering igual que en train.py
    df["Culmen Ratio"] = (
        df["Culmen Length (mm)"] /
        df["Culmen Depth (mm)"]
    )

    prediction = model.predict(df)

    return {
        "prediccion": prediction[0]
    }
