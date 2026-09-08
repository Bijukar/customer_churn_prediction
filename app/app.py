import streamlit as st
import requests



st.set_page_config(
    page_title="Customer Churn Prediction",
    layout='centered'
)

st.title("Customer Churn Prediction Application")
st.write("Enter Customer details to predict whether the customer will churn.")

# input data fields
gender=st.selectbox("Gender",['Male','Female'])
senior=st.selectbox("Senior Citizen",[0,1])
partner=st.selectbox("Partner",['Yes','No'])
Dependents=st.selectbox("Dependents",['Yes','No'])
tenure=st.slider('Tenure(months)',0,100,10)
Phoneservice=st.selectbox('Phone Service',['Yes','No'])
multiplelines=st.selectbox('Multiple Lines',['Yes','No','No phone service'])
internetservice=st.selectbox('Internet Service',['DSL','Fiber optic','No'])
OnlineSecurity=st.selectbox('Online Security',['Yes','No','No internet service'])
onlinebackup=st.selectbox('Online Backup',['Yes','No','No internet service'])
DeviceProtection=st.selectbox('Device Protection',['Yes','No','No internet service'])
techsupport=st.selectbox('Tech Support',['Yes','No','No internet service'])
streamingtv=st.selectbox('Streaming TV',['Yes','No','No internet service'])
streamingmovies=st.selectbox('Streaming Movies',['Yes','No','No internet service'])
contract=st.selectbox('Contract',['Month-to-month','One year','Two year'])
paperlessbilling=st.selectbox('Paperless Billing',['Yes','No'])
paymentmethod=st.selectbox('Payment Method',['Electronic check','Mailed check','Credit card (automatic)','Bank transfer (automatic)'])
monthlycharges=st.number_input('Monthly Charges',min_value=0.0,max_value=200.0)
totalcharges=st.number_input('Total Charges',min_value=0,max_value=10000)


if st.button('Predict Churn'):
    data={
        "gender":gender,
        "SeniorCitizen": senior,
        "Partner":partner,
        "Dependents":Dependents,
        "tenure":tenure,
        "PhoneService":Phoneservice,
        "MultipleLines":multiplelines,
        "InternetService":internetservice,
        "OnlineSecurity":OnlineSecurity,
        "OnlineBackup":onlinebackup,
        "DeviceProtection":DeviceProtection,
        "TechSupport":techsupport,
        "StreamingTV": streamingtv,
        "StreamingMovies": streamingmovies,
        "Contract": contract,
        "PaperlessBilling": paperlessbilling,
        "PaymentMethod": paymentmethod,
        "MonthlyCharges": monthlycharges,
        "TotalCharges": totalcharges
    }

    try:
        response=requests.post('https://customer-churn-prediction-sbnz.onrender.com/predict',json=data)
        if response.status_code==200:
            json_response=response.json()   #return pydn form from fastapi to json format
            prediction=json_response['prediction']
            prob=json_response['probability']
            if prediction==1:
                st.error("Customer is likely to Churn")
                st.metric("Churn Probability",f'{prob*100}%')
                st.progress(prob) 
            else:
                st.success("Customer is unlikely to Churn")
                st.metric("Churn Probability",f'{prob*100}%')
                st.progress(prob)
        else:
            st.error(f'API Error: {response.text}')
    except requests.exceptions.ConnectionError:
        st.error("cannot connect to FastAPI\n,Make sure the API server is running")