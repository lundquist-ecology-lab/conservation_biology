import streamlit as st
import os

# Function to load existing answers from a file
def load_answers(file_path="ecosystem_services.txt"):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

# Function to save answers to a file
def save_answers(answers, file_path="ecosystem_services.txt"):
    with open(file_path, "w") as file:
        for answer in answers:
            file.write(f"{answer}\n")

def page0_content():
    # Page Title
    st.title("Understanding the Value of Species through Environmental Economics")

    # Introduction
    st.header("Introduction")
    st.write("""
    Environmental economics explores how to balance human activities with environmental preservation.
    One key aspect is understanding the value of species – not just in terms of monetary worth but also in their roles in ecosystems.
    """)

    # Concept Explanation
    st.subheader("Key Concepts")
    st.write("""
    Species provide various ecosystem services, including:
    - **Provisioning services**: Products like food, fresh water, and medicinal resources.
    - **Regulating services**: Climate regulation, water purification, and pest control.
    - **Cultural services**: Recreational, spiritual, and aesthetic benefits.
    - **Supporting services**: Nutrient cycling, soil formation, and pollination.
    """)

    st.write("How many examples of ecosystem services can you think of?")
    
    # Load existing answers from the file
    st.session_state['ecosystem_services'] = load_answers()

    # Text input for user to enter their answer
    answer = st.text_input("Enter an example of an ecosystem service:")

    # Button to submit the answer
    if st.button("Submit"):
        if answer:
            st.session_state['ecosystem_services'].append(answer)
            save_answers(st.session_state['ecosystem_services'])
            st.rerun()  # Refresh the page to display the new entry

    # Display the submitted answers as quotes
    st.subheader("Submitted Examples of Ecosystem Services:")
    for service in st.session_state['ecosystem_services']:
        st.markdown(f"> {service}")

    # Refresh button
    if st.button("Refresh"):
        st.rerun()

    # Clear button (light red)
    clear_button_style = """
    <style>
    .stButton > button:nth-child(4) {
        background-color: #ffcccc;
        color: black;
    }
    </style>
    """
    st.markdown(clear_button_style, unsafe_allow_html=True)
    
    if st.button("Clear All"):
        st.session_state['ecosystem_services'] = []
        save_answers(st.session_state['ecosystem_services'])  # Clear the file
        st.rerun()