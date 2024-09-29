import streamlit as st

def page1_content():
    st.header("Biodiversity Map")
    st.components.v1.iframe("https://mol.org/patterns/richnessrarity", width=None, height=600)

