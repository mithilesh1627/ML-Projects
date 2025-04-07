import pickle
import numpy as np
import streamlit as st
import os
#column = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,condition]

model_path = os.path.join(os.path.dirname(__file__), 'training_model.svg')

st.title("Heart Disease Prediction Web App")
with open(model_path, 'rb') as file:
    loader = pickle.load(file)

def disease_prediction(input_data):
    input_data_np_reshape=np.asarray(input_data).reshape(1,-1)
    predict = loader.predict(input_data_np_reshape)
    if predict[0] != 0:
        st.toast("The person has Heart Disease")
    else:
        st.toast("The person doesn't has Heart Disease")

with st.form('form'):
    # age: age in years
    age = st.number_input("Enter the age of person")
    # sex: sex (1 = male; 0 = female)
    sex = st.radio("Gender of person ", options=['Male','Female'],
                   key='sex_radio',horizontal=True)
    sex_numeric = 1 if sex == 'Male' else 0
    # cp: chest pain type
    # -- Value 0: typical angina
    # -- Value 1: atypical angina
    # -- Value 2: non-anginal pain
    # -- Value 3: asymptomatic
    cp_options = {"Typical Angina": 0,
                  "Atypical Angina": 1,
                  "Non-anginal Pain": 2,
                  "Asymptomatic": 3}
    Chest_Pain = st.radio("Choose the type of chest pain",
                          options=list(cp_options.keys()),
                          key='chest_pain_radio',horizontal=True)
    cp_value = cp_options[Chest_Pain]
    # trestbps: resting blood pressure (in mm Hg on admission to the hospital)
    trestbps = st.number_input("Trestbps : Resting blood pressure (in mm Hg on admission to the hospital)")
    # chol: serum cholestoral in mg/dl
    chol = st.number_input("Serum cholestoral in mg/dl")
    # fbs: (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
    fbs = st.radio("Fasting blood sugar > 120 mg/dl",options=["Yes","No"],horizontal=True)
    fbs_numerical = 1 if fbs =="Yes" else 0
    # restecg: resting electrocardiographic results
    # -- Value 0: normal
    # -- Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
    # -- Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria
    restecg_options = {"Normal": 0,
                  "ST-T wave abnormality": 1,
                  "probable or definite left ventricular": 2}
    restecg = st.radio("Resting electrocardiographic results",
                       options=restecg_options.keys(),
                       horizontal=True)
    restecg_numerical = restecg_options[restecg]
    # thalach: maximum heart rate achieved
    thalach = st.number_input("Maximum heart rate achieved:")
    # exang: exercise induced angina (1 = yes; 0 = no)
    exang = st.radio("Exercise induced angina",
                     options=['Yes','No'],
                     horizontal=True)
    exang_numerical = 1 if fbs == "Yes" else 0
    # oldpeak = ST depression induced by exercise relative to rest
    oldpeak = st.number_input("ST depression")
    # slope: the slope of the peak exercise ST segment
    # -- Value 0: upsloping
    # -- Value 1: flat
    # -- Value 2: downsloping
    slope_option = {"upsloping":0,
                    "flat":1,
                    "downsloping":2}
    slope = st.radio("the slope of the peak exercise ST segment",
                     options=slope_option.keys(),
                     horizontal=True)
    slope_numerical = slope_option[slope]
    # ca: number of major vessels (0-3) colored by flourosopy
    ca = st.number_input("Number of major vessels")
    # thal: 0 = normal; 1 = fixed defect; 2 = reversable defect
    thal_option = {'normal':0,
                   'fixed defect':1,
                   'reversable defect':2}
    thal = st.radio("thal",options=thal_option.keys(),
                    horizontal=True)
    thal_numerical = thal_option[thal]
    form_list = [age,sex_numeric,cp_value,
                 trestbps,chol,fbs_numerical,
                 restecg_numerical,thalach,exang_numerical,oldpeak,
                 slope_numerical,ca,thal_numerical]
    if st.form_submit_button('predict'):
        disease_prediction(form_list)