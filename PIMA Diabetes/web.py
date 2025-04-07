import pickle
import numpy as np
import streamlit as st

<<<<<<< HEAD:web.py
loader = pickle.load(open('PIMA Diabetes/training_model.sav', 'rb'))
=======
loader = pickle.load(open('training_model.sav', 'rb'))
>>>>>>> b2efe55... remove web.py file to PIMA Diabetes folder:PIMA Diabetes/web.py

def diabetes_prediction(input_data):
    input_data_np_reshape=np.asarray(input_data).reshape(1,-1)
    predict = loader.predict(input_data_np_reshape)
    if predict[0] != 0:
        return "The person is diabetic"
    else:
        return "The person is not diabetic"


input_ = (8,183,64,0,0,23.3,0.672,32)
print(diabetes_prediction(input_))
# ['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']


def main():
    # give the title
    st.title("Diabetes Prediction Web App")
    # getting the input data from the user
    Pregnancies = st.number_input("Number of Pregnancies")
    Glucose = st.number_input("Glucose value")
    BloodPressure = st.number_input("Enter Blood Pressure value")
    SkinThickness = st.number_input("Enter Skin Thickness value")
    Insulin = st.number_input("Insulin value")
    BMI = st.number_input("BMI value")
    DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function value")
    Age = st.number_input("Age of person")

    # code for Prediction
    diagnosis = ''
    # creating the button for prediction
    if st.button("Diabetes Test Result"):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        st.toast(diagnosis,)


if __name__ =="__main__":
    main()
