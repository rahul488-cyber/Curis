import streamlit as st
from main import kick_off_the_crew
import time
st.header('Input Details About your injury', divider='gray')


with st.form("injury_details"):
    uploaded_file = st.file_uploader("Drop or Upload a Picture of Patient's Injury ")
    patients_name = st.text_input("Patients Name")
    age = st.slider("Patient's Age", 0, 100, 1)
    gender = st.selectbox(
    "Patient's Gender",
    ("Male", "Female", "Others(Neither Male nor Female)"),
    placeholder="Select gender...",
    )
    source_of_injury = st.text_input("Source of Injury")
    pain_level = st.slider("Injury Pain Level", 0, 10, 1)
    prior_medical_conditions = st.text_area(
        "Prior Medical Condition(s)",
    )
    additional_desc = st.text_area(
        "Additional Information about patient or injury",
    )
    medicine_list = st.text_input(
        "A list of Avaiable Medicines",
    )
    submitted = st.form_submit_button('Submit details')


if submitted:
    with open('injury_image.jpg', 'wb') as jammer:
        jammer.write(uploaded_file.read())
    agent_kickoff = kick_off_the_crew(
        patients_name, age, gender, source_of_injury, pain_level, prior_medical_conditions, additional_desc, medicine_list
    )
    # time.sleep(10)
    st.balloons()