from fastapi import FastAPI
from pydantic import BaseModel

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from src.prediction import predict_order


app = FastAPI(
    title="Qafza Order Delay Prediction API",
    version="1.0"
)


class OrderRequest(BaseModel):
    customer_state: str
    payment_types: str
    item_count: float
    total_item_price: float
    total_freight_value: float
    unique_products: float
    unique_sellers: float
    payment_records: float
    max_installments: float
    purchase_month: int
    purchase_dayofweek: int
    purchase_hour: int
    estimated_delivery_days: int


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/model-info")
def model_info():
    return {
        "model": "Logistic Regression",
        "version": "1.0"
    }


@app.post("/predict")
def predict(order: OrderRequest):
    return predict_order(order.model_dump())