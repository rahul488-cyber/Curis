import streamlit as st

with open('/Users/macromrit/Documents/Curis/injury-report-analysis.md', 'r') as jammer:
    details = jammer.read()


st.markdown(
    details
)