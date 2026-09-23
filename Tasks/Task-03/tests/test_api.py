from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_model_info():
    response = client.get("/model-info")

    assert response.status_code == 200
    assert response.json()["model"] == "Logistic Regression"
    assert response.json()["version"] == "1.0"


def test_predict():
    order = {
        "customer_state": "SP",
        "payment_types": "credit_card",
        "item_count": 3.0,
        "total_item_price": 134.97,
        "total_freight_value": 8.49,
        "unique_products": 1.0,
        "unique_sellers": 1.0,
        "payment_records": 1.0,
        "max_installments": 1.0,
        "purchase_month": 9,
        "purchase_dayofweek": 3,
        "purchase_hour": 12,
        "estimated_delivery_days": 19
    }

    response = client.post("/predict", json=order)

    assert response.status_code == 200

    result = response.json()

    assert "prediction" in result
    assert "probability" in result
    assert "model_version" in result