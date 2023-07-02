import pickle
import streamlit as st

# loading the saved heart disease model
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

# page title
st.title('CardioCare')
st.subheader('Heart Disease Prediction using ML')


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
    sex = st.selectbox('0-Female, 1-Male', ('0', '1'))
    


with col3:
    st.markdown("**Chest Pain type- **")
    cp = st.selectbox('0: Typical angina, 1: Atypical angina, 2:Non-anginal',('0', '1','2'))

with col1:
    st.markdown("**Resting Blood Pressure**")
    trestbps = st.slider('', 30, 250, 120)

with col2:
    st.markdown("**Serum Cholesterol in mg/dl**")
    chol = st.slider('', 10,500,120)

with col3:
    st.markdown("**Fasting Blood Sugar > 120 mg/dl:**")
    fbs = st.selectbox('0-False, 1=True', ('0', '1'))
   

with col1:
    st.markdown("**Resting Electrocardiographic Results:**")
    restecg = st.selectbox('0 = normal, 1 = having ST-T wave abnormality, 2 = Left Ventricle Hypertrophy',('0', '1','2'))


with col2:
    st.markdown("**Maximum Heart Rate achieved**")
    thalach = st.slider('', 30, 250, 130)

with col3:
    st.markdown("**Exercise Induced Angina: **")
    exang = st.selectbox('1 = True, 0 = False',('0', '1'))

with col1:
    st.markdown("**Exercise Induced Angina: **")
    oldpeak = st.text_input('')

with col2:
    st.markdown("**Slope of the peak exercise ST segment:**")
    slope = st.selectbox(' 0 = upsloping: better heart rate with excercise (uncommon), 1 = flat: minimal change (typical healthy heart), 2 = downsloping: signs of unhealthy heart',('0', '1','2'))

with col3:
    st.markdown("**Major vessels colored by flourosopy**")
    ca = st.selectbox('',('0', '1','2'))

with col1:
    st.markdown("**Thalassemia:**")
    thal = st.slider('1,3 = normal, 6 = fixed defect, 7 = reversible defect: no proper blood movement when excercising', 1,7,2)

# code for prediction
heart_diagnosis = ''

# creating a button for prediction
if st.button('Heart Disease Test Result'):
    heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    if heart_prediction[0] == 1:
        heart_diagnosis = 'The person is having heart disease.'
    else:
        heart_diagnosis = '🎉The person does not have any heart disease.'

st.success(heart_diagnosis)
import streamlit as st
import streamlit_webrtc as webrtc
from streamlit_webrtc import VideoTransformerBase, VideoFrame

# Custom video transformer class to capture screenshot
class ScreenshotTransformer(VideoTransformerBase):
    def __init__(self):
        self.screenshot = None

    def transform(self, frame: VideoFrame) -> VideoFrame:
        # Capture the first frame as a screenshot
        if self.screenshot is None:
            self.screenshot = frame.to_image()
            st.stop()

        return frame

# Main application code
def main():
    # Set up Streamlit
    st.title("Webpage Screenshot Downloader")

    # Initialize the video transformer
    transformer = ScreenshotTransformer()

    # Configure the video capture
    webrtc_ctx = webrtc.Streamer(
        video_transformer_factory=transformer,
        desired_playing_width=640,
        key="screenshot"
    )

    # Display the video capture
    webrtc_ctx.video_transformer = transformer
    webrtc_ctx.update()
    video_frame = webrtc_ctx.video_frame

    # Display the captured screenshot
    if video_frame is not None:
        st.image(video_frame.to_image(), use_column_width=True)

        # Create a download button for the image
        download_button_str = f"Download Screenshot"
        download_as = "screenshot.png"
        st.download_button(download_button_str, video_frame.to_image().save, args=(download_as,))

if __name__ == "__main__":
    main()
