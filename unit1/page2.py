import streamlit as st

def page2_content():
    st.header("Major global issues in Conservation Biology")
    st.write("Global population clock")
    st.components.v1.iframe("https://www.worldometers.info/world-population/", width=None, height=600, scrolling=True)

