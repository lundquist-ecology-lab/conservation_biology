import streamlit as st
from PIL import Image, UnidentifiedImageError
import requests
from io import BytesIO
import pandas as pd
import os

# Path to the CSV file
CSV_FILE_PATH = 'user_selections.csv'

# Initialize session state for collecting data
def initialize_session_state():
    if 'selection_data' not in st.session_state:
        if os.path.exists(CSV_FILE_PATH):
            st.session_state['selection_data'] = pd.read_csv(CSV_FILE_PATH)
        else:
            st.session_state['selection_data'] = pd.DataFrame(
                {"Image": ["A", "B", "C", "D", "E", "F", "G", "H"], "User_Selected_Count": [0]*8}
            )

    if 'selected_images' not in st.session_state:
        st.session_state['selected_images'] = {}

    if 'reveal_answer' not in st.session_state:
        st.session_state['reveal_answer'] = False

# Function to save the DataFrame to CSV
def save_data_to_csv():
    st.session_state['selection_data'].to_csv(CSV_FILE_PATH, index=False)

# Function to clear the CSV file and reload the table
def clear_csv():
    # Reset the DataFrame to its initial state
    st.session_state['selection_data'] = pd.DataFrame(
        {"Image": ["A", "B", "C", "D", "E", "F", "G", "H"], "User_Selected_Count": [0]*8}
    )
    # Save the reset DataFrame to CSV
    save_data_to_csv()
    st.success("CSV file has been cleared!")

# Function to cache and fetch images
@st.cache_resource
def fetch_images():
    image_urls = {
        "A": "https://upload.wikimedia.org/wikipedia/commons/9/93/European_wasp_white_bg.jpg",
        "B": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/ARS_Megachile_rotundata.jpg/800px-ARS_Megachile_rotundata.jpg",
        "C": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Apis_mellifera_Tanzania.jpg/1024px-Apis_mellifera_Tanzania.jpg",
        "D": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/2013.04.24.-03-Kirschgartshaeuser_Schlaege_Mannheim-Gefleckter_Wollschweber_im_Flug.jpg/1920px-2013.04.24.-03-Kirschgartshaeuser_Schlaege_Mannheim-Gefleckter_Wollschweber_im_Flug.jpg",
        "E": "https://upload.wikimedia.org/wikipedia/commons/e/e3/Megachile_inimica_female_sunflower.jpg",
        "F": "https://upload.wikimedia.org/wikipedia/commons/3/32/Bee-apis.jpg",
        "G": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/ComputerHotline_-_Syrphidae_sp._%28by%29_%283%29.jpg/1024px-ComputerHotline_-_Syrphidae_sp._%28by%29_%283%29.jpg",
        "H": "https://upload.wikimedia.org/wikipedia/commons/7/7d/Honeybee_on_Lavender.jpg"
    }
    
    images = {}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    for key, url in image_urls.items():
        try:
            response = requests.get(url, headers=headers)  # Set custom headers with User-Agent
            response.raise_for_status()  # Check if request was successful
            img = Image.open(BytesIO(response.content))
            images[key] = img
        except (requests.exceptions.RequestException, UnidentifiedImageError) as e:
            st.error(f"Error loading image {key}: {e}")

    return images

# Function to handle periodic table updates
def table_update(table_placeholder):
    # Reload the latest data from the CSV file
    if os.path.exists(CSV_FILE_PATH):
        st.session_state['selection_data'] = pd.read_csv(CSV_FILE_PATH)

    # Update the table content dynamically
    table_placeholder.write("Current User Selections (Number of Times Each Image Was Chosen):")
    table_placeholder.dataframe(st.session_state['selection_data'])

# Function to display the content of the page
def page2_content():
    st.header("Identify the Real Honey Bees")
    st.write("Look at the images below. Select which ones you think are real honey bees.")

    initialize_session_state()
    images = fetch_images()

    for key in images.keys():
        if key not in st.session_state['selected_images']:
            st.session_state['selected_images'][key] = False

    with st.form(key='selection_form'):
        cols = st.columns(4)  # 4 columns for the grid

        for idx, (letter, img) in enumerate(images.items()):
            with cols[idx % 4]:
                st.image(img, caption=f"Image {letter}", use_column_width=True)
                st.session_state['selected_images'][letter] = st.checkbox(
                    f"Real Honey Bee: {letter}", 
                    value=st.session_state['selected_images'][letter], 
                    key=f"checkbox_{letter}"
                )

        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            selected = [letter for letter, selected in st.session_state['selected_images'].items() if selected]
            if selected:
                for letter in selected:
                    st.session_state['selection_data'].loc[
                        st.session_state['selection_data']["Image"] == letter, "User_Selected_Count"
                    ] += 1
                save_data_to_csv()
                st.write(f"You selected the following images as real honey bees: {', '.join(selected)}")
            else:
                st.write("You didn't select any images as real honey bees.")

    # Placeholder for dynamically updating the table
    table_placeholder = st.empty()
    table_update(table_placeholder)

    # Button to reveal the correct answer
    if st.button("Reveal Answer"):
        st.session_state['reveal_answer'] = True

    # Display the correct answer if the button is clicked
    if st.session_state['reveal_answer']:
        st.write("The correct images of real honey bees are: **C, F, and H**")

    # Button to clear the CSV file
    if st.button("Clear CSV"):
        clear_csv()
        table_update(table_placeholder)  # Update the table after clearing

    # Button to refresh the table
    if st.button("Refresh Table"):
        table_update(table_placeholder)  # Refresh the table when clicked
