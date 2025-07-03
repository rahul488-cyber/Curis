import streamlit as st

with open('/Users/macromrit/Documents/Curis/treatment_report.md', 'r') as jammer:
    details = jammer.read()


st.markdown(
    details
)