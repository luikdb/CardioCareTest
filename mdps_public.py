import pickle
import streamlit as st

# loading the saved heart disease model
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

# page title
st.title('Heart Disease Prediction using ML')

# getting the input data from the user
col1, col2, col3 = st.columns(3)

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False


with col1:
    age = st.text_input('Age')

with col2:
    sex = st.text_input('Sex')

with col3:
    cp = st.slider('Chest Pain type', 0, 3, 1)
    

with col1:
    trestbps = st.text_input('Resting Blood Pressure')

with col2:
    chol = st.text_input('Serum Cholesterol in mg/dl')

with col3:
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

with col1:
    restecg = st.text_input('Resting Electrocardiographic results', '0-2')

with col2:
    thalach = st.text_input('Maximum Heart Rate achieved')

with col3:
    exang = st.text_input('Exercise Induced Angina')

with col1:
    oldpeak = st.text_input('ST depression induced by exercise')

with col2:
    slope = st.text_input('Slope of the peak exercise ST segment')

with col3:
    ca = st.text_input('Major vessels colored by flourosopy', '0-3')

with col1:
    thal = st.text_input('thal', '0 = normal; 1 = fixed defect; 2 = reversable defect')

# code for prediction
heart_diagnosis = ''

# creating a button for prediction
if st.button('Heart Disease Test Result'):
    heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    if heart_prediction[0] == 1:
        heart_diagnosis = '⚠️The person is having heart disease.'
    else:
        heart_diagnosis = '🎉The person does not have any heart disease.'

st.success(heart_diagnosis)
