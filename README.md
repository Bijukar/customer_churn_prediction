# Customer Churn Prediction
A machine learning project that predicts whether a customer is likely to churn based on customer information. The trained ML pipeline is exposed through a FastAPI REST API, while Streamlit provides a simple web interface for users.

## 🚀 Project Overview
Customer churn prediction helps businesses identify customers who may stop using their services. This project uses a classification model to predict churn and also provides the probability of the prediction.

**The project follows a complete machine learning workflow:**
```
Data
 ↓
EDA & Data Analysis
 ↓
Data Preprocessing
 ↓
Feature Transformation
 ↓
Model Training
 ↓
Model Evaluation
 ↓
Save ML Pipeline
 ↓
FastAPI API
 ↓
Streamlit Web App
```

## ✨ Features
- Customer churn prediction
- Data preprocessing using Scikit-learn
- Categorical feature encoding
- Numerical feature preprocessing
- ML model saved as a reusable pipeline
- FastAPI REST API for predictions
- Prediction probability using predict_proba()
- Streamlit frontend
- API and frontend deployed separately
- Error handling for API and Streamlit
- Swagger API documentation through FastAPI

## 🛠️ Technologies Used
- Python
- Pandas – Data processing
- NumPy – Numerical operations
- Scikit-learn – Machine learning and preprocessing
- Joblib – Model serialization
- FastAPI – Backend REST API
- Uvicorn – ASGI server
- Pydantic – Request validation
- Streamlit – Web interface
- Render – FastAPI deployment
- Git & GitHub – Version control

## 📁 Project Structure

```markdown
customer_churn_prediction/
│
├── data/
│   └── Telco-Customer-Churn.csv
│
├── model/
│   ├── model.pkl
│
├── api/
|   |__ main.py
|
|___app/
│   └── app.py
│
├── notebooks/
│   ├── model.ipynb
│   ├── eda.ipymb
│
├── requirements.txt
├── README.md
└── .gitignore
```
## 🔄 How It Works

1. The Streamlit application collects customer information from the user and sends it to the FastAPI /predict endpoint.

2. FastAPI validates the input using Pydantic and converts the input into the format required by the trained ML pipeline.

3. The pipeline performs the required preprocessing and generates:

Churn prediction
Prediction probability
Example API response:
```
{
    "prediction": 1,
    "probability": 0.87,
    "message": "Customer is likely to churn."
}
```
Here:

1 = Customer is likely to churn
0 = Customer is unlikely to churn
probability = Probability of the predicted class

## 🧠 Machine Learning Pipeline
```
The preprocessing and model training workflow uses a Scikit-learn pipeline.

A typical pipeline can contain:

Raw Input
   ↓
ColumnTransformer
   ├── Numerical Features → Scaling
   └── Categorical Features → One-Hot Encoding 
   ↓
ML Classifier
   ↓
Prediction
The complete pipeline is saved using Joblib so that the same preprocessing is automatically applied during API prediction.

📡 FastAPI API
The main prediction endpoint is:

POST /predict
Example request:

{
    "gender": "Male",
    "age": 30,
    "tenure": 12,
    "monthly_charges": 50.0,
    "contract": "Month-to-month",
    "internet_service": "Fiber optic"
}
Example response:

{
    "prediction": 1,
    "probability": 0.87,
    "message": "Customer is likely to churn."
}

```

### ☁️ Deployment
```
The project uses separate deployments for the backend and frontend.

FastAPI
FastAPI is deployed on Render.

Render start command:

uvicorn main:app --host 0.0.0.0 --port $PORT
After deployment, Render provides an API URL such as:  [https://customer-churn-prediction-sbnz.onrender.com]


The Streamlit application sends requests to:

https://customer-churn-prediction-sbnz.onrender.com/predict
Streamlit
The Streamlit application can be deployed separately using Streamlit Community Cloud or another suitable hosting platform.
```

## 🎯 Learning Outcomes

Through this project, I learned how to:

1. Build an end-to-end machine learning workflow
2. Perform preprocessing and feature transformation
3. Create reusable Scikit-learn pipelines
4. Save and load trained ML models
5. Build REST APIs using FastAPI
6. Validate API requests using Pydantic
7. Connect a frontend with a machine learning API
8. Handle API errors
9. Deploy an ML API on Render
10. Deploy a Streamlit application


#### 👨‍💻 Author
*Biju Kar*

If you found this project useful, feel free to ⭐ the repository.
