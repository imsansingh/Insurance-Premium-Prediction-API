# Insurance-Premium-Prediction-API
A FastAPI-based machine learning API that predicts an insurance premium category based on user demographics and financial attributes. The project loads a pre-trained ML model and exposes a REST endpoint for real-time predictions.

## 📌 Features

🚀 FastAPI-powered REST API

🤖 Pre-trained machine learning model (model.pkl)

📊 Returns predicted category with confidence score

🐳 Dockerized for easy deployment

🧱 Clean modular project structure (model, schema, config)

## 📦 Tech Stack

Backend: FastAPI

ML: Scikit-learn, Pandas

Model Storage: Pickle

API Docs: Swagger (OpenAPI)

Deployment: Docker

## 🧠 Machine Learning Model

Type: Classification model (scikit-learn)

Input: User demographic & financial data

Output:

Predicted insurance premium category

Confidence score

Probability distribution across all classes

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Insurance_premium_prediction
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv myenv
   # Windows
   myenv\Scripts\activate
   # Linux/Mac
   source myenv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt


## Usage (Local)

Run the application using Uvicorn:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at `http://localhost:8000`.

## API Endpoints

### 1. Root
- **URL**: `/`
- **Method**: `GET`
- **Description**: Returns a welcome message.

### 2. Health Check
- **URL**: `/health`
- **Method**: `GET`
- **Description**: Returns the status of the API and model version.

### 3. Predict
- **URL**: `/predict`
- **Method**: `POST`
- **Description**: Predicts the insurance premium.
- **Request Body** (Example):
  ```json
  {
    "bmi": 25.5,
    "age_group": "25-30",
    "lifestyle_risk": "Low",
    "city_tier": "Tier-1",
    "income_lpa": 10.5,
    "occupation": "Salaried"
  }
  ```

## Docker

### Build the Image

```bash
docker build -t insurance-prediction .
```

### Run the Container

```bash
docker run -p 8000:8000 insurance-prediction
```

Access the API at `http://localhost:8000`.

## Documentation

FastAPI provides automatic interactive documentation. Once the app is running, visit:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
