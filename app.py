# Setup
import streamlit as st
import pandas as pd
import joblib

# Load model and test data
model_testdata = joblib.load('model_testdata.joblib')

model = model_testdata['model']
test_data = model_testdata['test_data']
test_data = test_data.reset_index()

# Creating User Interface

# title of the model
with st.container():

    # columns for image and title
    img_col, title_col = st.columns([1,2.5], border=False, vertical_alignment='center')

    # image
    with img_col:
        st.image('Images/logo.png', width=150)

    # title
    with title_col:
        st.write('# :rainbow[**TENSE LENS**] 🔍')
        st.write('**:blue[:red[TENSE LENS] is a supervised Machine Learning model developed using :red[LOGISTIC REGRESSION], which classifies sentences into different Tenses. ]**')    

# expander for some random text
with st.expander('**:blue[Demo Sentences]**',expanded=True):
    st.dataframe(test_data['Sentence'].sample(3).values, use_container_width=True, on_select='ignore')

# Container for Input and output
with st.container():
    text = st.text_area('**:blue[ENTER TEXT IN BELOW BOX]**', placeholder='Enter a sentence of minimum 10 words...!')

    output = st.empty()

    if not text.isspace():
        prediction = model.predict([text])

        if prediction == 1:
            output.success('**:green[PRESENT TENSE]**')
        elif prediction == 2:
            output.success('**:green[PAST TENSE]**')
        else:
            output.success('**:green[FUTURE TENSE]**')
    
# Container for sharing contents
with st.container():
     # five more cols for linking app with other platforms
    youtube_col, hfspace_col, madee_col, repo_col, linkedIn_col = st.columns([1,1.2,1.08,1,1], gap='small')

    # Youtube link
    with youtube_col:
        st.link_button('**VIDEO**', icon=':material/slideshow:', url='https://youtu.be/IDHr9Z4Q4iY', help='YOUTUBE')CLE
    
    # Hugging Face Space link
    with hfspace_col:
        st.link_button('**HF SPACE**', icon=':material/sentiment_satisfied:', url='https://huggingface.co/spaces/madhav-pani/Tense_Lens/tree/main', help='HUGGING FACE SPACE')

    # Madee Link
    with madee_col:
        st.button('**MADEE**', icon=':material/flight:', disabled=True, help='MADEE')

    # Repository Link
    with repo_col:
        st.link_button('**REPO**', icon=':material/code_blocks:', url='https://github.com/madhavpani/Tense_Lens', help='GITHUB REPOSITORY')

    # LinkedIn link
    with linkedIn_col:
        st.link_button('**CONNECT**', icon=':material/connect_without_contact:', url='https://www.linkedin.com/in/madhavpani', help='LINKEDIN')