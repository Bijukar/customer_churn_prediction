from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from fastapi.responses import JSONResponse
from typing import Literal
import pandas as pd
import numpy as np
import pickle


with open('D:\Resume Project\churn predction\models\model.pkl','rb')as f:
    model=pickle.load(f)
app=FastAPI()

class CustomerData(BaseModel):
    gender:Literal['Male','Female']
    SeniorCitizen:Literal[0,1] 
    Partner:Literal['Yes','No']
    Dependents:Literal['Yes','No']
    tenure:int=Field(...,ge=0,le=100)
    PhoneService:Literal['Yes','No']   
    MultipleLines:Literal['Yes','No','No phone service']
    InternetService:Literal['DSL','Fiber optic','No'] 
    OnlineSecurity:Literal['Yes','No','No internet service']  
    OnlineBackup:Literal['Yes','No','No internet service']
    DeviceProtection:Literal['Yes','No','No internet service']
    TechSupport:Literal['Yes','No','No internet service']    
    StreamingTV:Literal['Yes','No','No internet service']   
    StreamingMovies:Literal['Yes','No','No internet service']    
    Contract:Literal['Month-to-month','One year','Two year']    
    PaperlessBilling:Literal['Yes','No']   
    PaymentMethod:Literal['Electronic check','Mailed check','Credit card (automatic)','Bank transfer (automatic)']    
    MonthlyCharges:float=Field(...,ge=0,le=200)
    TotalCharges:float=Field(...,ge=0,le=10000)



@app.get('/home')
def home():
    return{'message':'Customer churn prediction API is running'}

@app.post('/predict')
async def predict(customer:CustomerData):
    try:
      data=customer.model_dump()
      data_df=pd.DataFrame([data])      
      prediction=model.predict(data_df)[0] 
      probability=model.predict_proba(data_df)[0]
      return {
        'prediction':int(prediction),
        'probability': float(probability[prediction])
    
      }
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"prediction failed:{str(e)}")

