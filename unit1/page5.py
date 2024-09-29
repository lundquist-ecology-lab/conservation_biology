import streamlit as st

def page5_content():
    st.header("Major global issues in Conservation Biology")
    st.write("What is your Ecological Footprint?")
    st.components.v1.iframe("https://www.footprintcalculator.org/home/en", width=None, height=600)