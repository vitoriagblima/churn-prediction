import os
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# ======================================
# Inicialização da API
# ======================================
app = FastAPI(
    title="API de Predição de Churn",
    description="API para prever risco de churn de clientes ERP",
    version="1.0.0"
)

# ======================================
# Health check (Render usa isso)
# ======================================
@app.get("/")
def root():
    return {"status": "API de churn rodando"}

@app.get("/healthz")
def health():
    return {"status": "ok"}

# ======================================
# Caminho do modelo (compatível com Docker)
# ======================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(
    BASE_DIR, "..", "models", "best_random_forest.pkl"
)

# ======================================
# Lazy loading do modelo
# ======================================
modelo = None

def carregar_modelo():
    global modelo
    if modelo is None:
        modelo = joblib.load(MODEL_PATH)

# ======================================
# Esquema de entrada
# ======================================
class Cliente(BaseModel):
    data: dict

# ======================================
# Endpoint de predição
# ======================================
@app.post("/predict")
def predict(cliente: Cliente):
    carregar_modelo()

    # Converte entrada em DataFrame
    df = pd.DataFrame([cliente.data])

    # Predição
    probabilidade = modelo.predict_proba(df)[:, 1][0]
    churn_predito = int(probabilidade >= 0.15)

    return {
        "probabilidade_churn": round(float(probabilidade), 4),
        "churn_predito": churn_predito
    }
