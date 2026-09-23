from pathlib import Path
import logging

import joblib
import pandas as pd
import yaml


BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config" / "config.yaml"


# Load configuration
with open(CONFIG_PATH, "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)


# Logging
logging.basicConfig(
    level=config["logging"]["level"],
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


# Paths from config
MODEL_PATH = BASE_DIR / config["model"]["path"]
PREPROCESSOR_PATH = BASE_DIR / config["preprocessor"]["path"]

MODEL_VERSION = config["model"]["version"]


# Load saved artifacts
logger.info("Loading model and preprocessor...")

model = joblib.load(MODEL_PATH)
preprocessor = joblib.load(PREPROCESSOR_PATH)

logger.info("Model and preprocessor loaded successfully.")


LABELS = {
    0: "On-time",
    1: "Late"
}


def predict_order(order_data: dict) -> dict:
    input_df = pd.DataFrame([order_data])

    processed_data = preprocessor.transform(input_df)

    prediction = int(model.predict(processed_data)[0])

    probabilities = model.predict_proba(processed_data)[0]

    probability = float(probabilities[prediction])

    result = {
        "prediction": LABELS[prediction],
        "probability": round(probability, 4),
        "model_version": MODEL_VERSION
    }

    logger.info(
        "Prediction=%s | Probability=%.4f | Model version=%s",
        result["prediction"],
        result["probability"],
        result["model_version"]
    )

    return result


if __name__ == "__main__":

    example_order = {
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

    print(predict_order(example_order))