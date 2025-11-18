import streamlit as st
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
import pickle


#Load the ANN trained model
model=tf.keras.models.load_model('model.h5')

#Load the Scaler object with pickle extension

with open('scaler.pkl','rb') as file:
    scaler=pickle.load(file)

#app title
st.title("Diabetes Prediction")


#User_inputs

Pregnancies = st.slider("Pregnancies", min_value=0, max_value=20, value=1)

Glucose = st.slider("Glucose", min_value=0, max_value=300, value=120)
BloodPressure = st.slider("BloodPressure", min_value=0, max_value=150, value=70)
SkinThickness = st.slider("SkinThickness", min_value=0, max_value=100, value=20)
Insulin = st.slider("Insulin", min_value=0, max_value=900, value=80)
BMI = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0, step=0.1)
DiabetesPedigreeFunction = st.number_input(
    "Diabetes Pedigree Function",
    min_value=0.0, max_value=5.0, value=0.5, step=0.001
)
Age = st.slider("Age", min_value=1, max_value=120, value=30)


input_data=pd.DataFrame({
    
    "Pregnancies":[Pregnancies],
    "Glucose":[Glucose],
    "BloodPressure":[BloodPressure],
    "SkinThickness": [SkinThickness],
    "Insulin":[Insulin],
    "BMI":[BMI],
    "DiabetesPedigreeFunction":[DiabetesPedigreeFunction],
    "Age":[Age]

})

input_data_scaled=scaler.transform(input_data)

#Prediction

prediction=model.predict(input_data_scaled)
prediction_probability=float(prediction[0][0])

st.subheader(f"Prediction Probability:**{prediction_probability:.4f}**")

if(prediction_probability>0.5):
    st.error("Person likely to have diabetes")
else:
    st.success("Person unlikely to have diabetes")