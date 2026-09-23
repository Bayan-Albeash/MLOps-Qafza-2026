Yes — make the whole README fully English. Use this version:

````markdown
# Task 03 - From Notebooks to Production

This project converts the trained order delay prediction model from Task 02 into a production-style inference service.

## Goal

Given a new order, the service predicts whether the order will be:

- On-time
- Late

The API also returns:

- Prediction probability
- Model version

## Project Structure

```text
Task-03/
├── app/
│   └── main.py
├── config/
│   └── config.yaml
├── data/
├── models/
│   ├── logistic_regression_model.joblib
│   ├── preprocessor.joblib
│   └── feature_list.txt
├── requirements/
│   ├── requirements.txt
│   └── requirements-dev.txt
├── src/
│   └── prediction.py
├── tests/
│   └── test_api.py
├── Dockerfile
└── README.md
````

## Inference Pipeline

The service loads the saved fitted preprocessing pipeline and the trained Logistic Regression model.

No model training or fitting happens during inference.

The workflow is:

```text
New Order
    ↓
Saved Preprocessor
    ↓
Processed Features
    ↓
Logistic Regression Model
    ↓
Prediction + Probability + Model Version
```

## Configuration

The project uses a YAML configuration file:

```text
config/config.yaml
```

The configuration file stores:

* Model path
* Preprocessor path
* Model version
* API settings
* Logging level

This avoids hardcoding important configuration values inside the Python code.

## Model

Model type:

```text
Logistic Regression
```

Model version:

```text
1.0
```

The trained model and fitted preprocessing objects were created in Task 02 and are loaded during inference.

## API

The inference service is built using FastAPI.

Available routes:

* `GET /health`
* `GET /model-info`
* `POST /predict`

### Run the API locally

From the repository root:

```bash
uvicorn app.main:app --app-dir Tasks/Task-03 --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

FastAPI automatically provides interactive Swagger API documentation.

## Prediction Example

Example request:

```json
{
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
```

Example response:

```json
{
  "prediction": "On-time",
  "probability": 0.7647,
  "model_version": "1.0"
}
```

## Testing

The project uses `pytest` for automated testing.

Current tests include:

* Health endpoint test
* Model information endpoint test
* Prediction endpoint test

Run the tests with:

```bash
python -m pytest tests/test_api.py -v
```

Current result:

```text
3 passed
```

## Docker

The API can also run inside a Docker container.

### Build the Docker image

From the `Task-03` directory:

```bash
docker build -t qafza-task3 .
```

### Run the Docker container

```bash
docker run -p 8001:8000 qafza-task3
```

Then open:

```text
http://127.0.0.1:8001/docs
```

## Logging

The project uses Python's `logging` library instead of print statements for service events.

The service currently logs:

* Model loading
* Preprocessor loading
* Prediction result
* Prediction probability
* Model version

## Requirements

Runtime dependencies are stored in:

```text
requirements/requirements.txt
```

Development and testing dependencies are stored in:

```text
requirements/requirements-dev.txt
```

## Current Implementation

The current implementation includes:

* Structured project repository
* Configuration file
* Saved model loading
* Saved preprocessor loading
* Python inference module
* FastAPI service
* Health endpoint
* Model information endpoint
* Prediction endpoint
* Input validation using Pydantic
* Logging
* Automated API tests
* Docker image
* Docker container execution
* Swagger API documentation

## Important Note

Training is not performed inside the inference service.

The service only loads the already trained model and fitted preprocessing objects from Task 02 and uses them to make predictions on new orders.

```

This version is completely English and more suitable for GitHub submission.
```
