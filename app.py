import streamlit as st

from unit1.page0 import page0_content as u10
from unit1.page1 import page1_content as u11
from unit1.page2 import page2_content as u12
from unit1.page3 import page3_content as u13
from unit1.page4 import page4_content as u14
from unit1.page5 import page5_content as u15
from unit1.page6 import page6_content as u16
from unit1.page7 import page7_content as u17
from unit1.page8 import page8_content as u18

from unit2.page0 import page0_content as u20
from unit2.page1 import page1_content as u21
from unit2.page2 import page2_content as u22
from unit2.page3 import page3_content as u23
from unit2.page4 import page4_content as u24
from unit2.page5 import page5_content as u25

from unit3.page0 import page0_content as u30
from unit3.page1 import page1_content as u31
from unit3.page2 import page2_content as u32

from paper_summary.page0 import page0_content as up0

# Set the page configuration for the Streamlit app
st.set_page_config(page_title="Conservation Biology", layout="wide")

# Inject CSS to hide unwanted elements
st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;} /* Hide the Streamlit main menu */
        .stDeployButton {visibility: hidden;} /* Hide the deploy button */
        footer {visibility: hidden;} /* Hide the footer */
        #stDecoration {display:none;} /* Hide other unwanted decorations */
    </style>
""", unsafe_allow_html=True)

# Set the title for the navigation sidebar
st.sidebar.title("Navigation")

# Create a sidebar menu for main navigation
main_page = st.sidebar.selectbox("Choose a unit:", ["Home", 
                                                    "Introduction to Conservation Biology",
                                                    "Biodiversity",
                                                    "Valuing Biodiversity",
                                                    "Paper Summary 1"])

# Subpage selection based on the main presentation
if main_page == "Home":
    st.title("Welcome to the Interactive Site for Conservation Biology")
    st.write("Choose a unit from the sidebar to view its content.")
    st.write("Author: Matthew J. Lundquist, PhD")
    # HTML and CSS for dynamic resizing and centering
    html_code = """
    <div style="display: flex; justify-content: center; width: 100%; margin-bottom: 20px;">
        <div style="width: 50%;">
            <img src="https://images.unsplash.com/photo-1525382455947-f319bc05fb35?q=80&w=1496&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" style="width: 100%;">
        </div>
    </div>
    """
    
    # Render the HTML
    st.markdown(html_code, unsafe_allow_html=True)
    
elif main_page == "Introduction to Conservation Biology":
    sub_page = st.sidebar.radio("Choose a page:", ["What is the most important environmental issue?",
                                                   "Human Population Growth", 
                                                   "Population Clock", 
                                                   "Ecological Footprints", 
                                                   "Ecological Footprint by Land Type", 
                                                   "What is your Ecological Footprint?", 
                                                   "Key People in early Conservation Biology", 
                                                   "Terms for Discussion",
                                                   "Organizational Values"])
    
    if sub_page == "What is the most important environmental issue?":
        u10()
    elif sub_page == "Human Population Growth":
        u11()
    elif sub_page == "Population Clock":
        u12()
    elif sub_page == "Ecological Footprints":
        u13()
    elif sub_page == "Ecological Footprint by Land Type":
        u14()
    elif sub_page == "What is your Ecological Footprint?":
        u15()
    elif sub_page == "Key People in early Conservation Biology":
        u16()
    elif sub_page == "Terms for Discussion":
        u17()
    elif sub_page == "Organizational Values":
        u18()

elif main_page == "Biodiversity":
    sub_page = st.sidebar.radio("Choose a page:", ["Introduction",
                                                   "Patterns of Biodiversity",
                                                   "Identifying Species",
                                                   "Quantifying Biodiversity",
                                                   "Genetic Diversity",
                                                   "Trophic dynamics"
                                                    ])
    
    if sub_page == "Introduction":
        u20()
    elif sub_page == "Patterns of Biodiversity":
        u21()
    elif sub_page == "Identifying Species":
        u22()
    elif sub_page == "Quantifying Biodiversity":
        u23()
    elif sub_page == "Genetic Diversity":
        u24()
    elif sub_page == "Trophic dynamics":
        u25()
    
elif main_page == "Valuing Biodiversity":
    sub_page = st.sidebar.radio("Choose a page:", ["Ecosystem Services",
                                                   "Valuation Activity",
                                                   "Environmental Ethics"
                                                    ])
    
    if sub_page == "Ecosystem Services":
        u30()
    elif sub_page == "Valuation Activity":
        u31()
    elif sub_page == "Environmental Ethics":
        u32()
        
elif main_page == "Paper Summary 1":
    sub_page = st.sidebar.radio("Choose a page:", ["Discussion"])
    
    if sub_page == "Discussion":
        up0()