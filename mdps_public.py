import pickle
import streamlit as st

# loading the saved heart disease model
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

# page title
st.title('CardioCare')
st.header(':red[Cardio]:white[Care]')
st.header('Heart Disease Prediction using ML')


# getting the input data from the user
col1, col2, col3 = st.columns(3)

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False


with col1:
    st.markdown("**Age**")
    age = st.slider('', 1,110,18)


with col2:

    st.markdown("**Sex**")
    sex = st.slider('0-Female, 1=Male', 0, 1, 1)



with col3:
    st.markdown("**Chest Pain type- **")
    cp = st.slider('0: Typical angina, 1: Atypical angina, 2:Non-anginal',0,2,1)

with col1:
    st.markdown("**Resting Blood Pressure**")
    trestbps = st.slider('', 30, 250, 120)

with col2:
    st.markdown("**Serum Cholesterol in mg/dl**")
    chol = st.slider('', 10,500,120)

with col3:
    st.markdown("**Fasting Blood Sugar > 120 mg/dl:**")
    fbs = st.slider('0-False, 1=True', 0, 1, 1)
   

with col1:
    st.markdown("**Resting Electrocardiographic Results:**")
    restecg = st.slider('0 = normal, 1 = having ST-T wave abnormality, 2 = Left Ventricle Hypertrophy', 0,2,1)


with col2:
    st.markdown("**Maximum Heart Rate achieved**")
    thalach = st.slider('', 30, 250, 130)

with col3:
    st.markdown("**Exercise Induced Angina: **")
    exang = st.slider('1 = True, 0 = False', 0,1,1)

with col1:
    st.markdown("**Exercise Induced Angina: **")
    oldpeak = st.text_input('')

with col2:
    st.markdown("**Slope of the peak exercise ST segment:**")
    slope = st.slider(' 0 = upsloping: better heart rate with excercise (uncommon), 1 = flat: minimal change (typical healthy heart), 2 = downsloping: signs of unhealthy heart', 0,2,1)

with col3:
    st.markdown("**Major vessels colored by flourosopy**")
    ca = st.slider('', 0,3,1)

with col1:
    st.markdown("**Thalassemia:**")
    thal = st.slider('1,3 = normal, 6 = fixed defect, 7 = reversible defect: no proper blood movement when excercising', 1,7,2)

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
