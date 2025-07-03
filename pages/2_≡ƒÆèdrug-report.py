import streamlit as st

with open('/Users/macromrit/Documents/Curis/medicine-report-analysis.md', 'r') as jammer:
    details = jammer.read()


st.markdown(
    details
)