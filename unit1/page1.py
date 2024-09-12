import streamlit as st

def page1_content():
    st.header("Major global issues in Conservation Biology")
    st.write("Human population growth")
    st.components.v1.iframe("https://ourworldindata.org/grapher/population", width=None, height=600)


