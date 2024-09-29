import streamlit as st
import os
import json
import shutil
from datetime import datetime

# Define the file names
file_name_terms_json = "conservation_biology_terms.json"
backup_dir = "backups"  # Backup directory

# Function to save conservation biology terms to a JSON file (append mode)
def save_to_json(data, file_name=file_name_terms_json):
    # Load existing data
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            try:
                existing_data = json.load(f)
            except json.JSONDecodeError:
                existing_data = {}
    else:
        existing_data = {}

    # Merge new data with existing data
    combined_data = {**existing_data, **data}

    # Save the combined data to the JSON file
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(combined_data, f, ensure_ascii=False, indent=4)
    st.success(f"Results successfully appended to JSON file: {file_name}")

# Function to display the content of a JSON file
def display_json(file_name):
    try:
        if not os.path.exists(file_name):
            st.error(f"File {file_name} not found.")
            return 0  # Return zero if the file is not found

        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Display each term in a separate container for better readability
        for term, content in data.items():
            with st.container():
                st.markdown(f"### {term}")
                st.markdown(f"**What is it?** <br>{content['what']}", unsafe_allow_html=True)
                st.markdown(f"**Pros:** <br>{content['pros']}", unsafe_allow_html=True)
                st.markdown(f"**Cons:** <br>{content['cons']}", unsafe_allow_html=True)
                st.markdown("---")  # Divider between terms

        # Provide a download button for JSON file
        json_data = json.dumps(data, ensure_ascii=False, indent=4)
        st.download_button(
            label="Download JSON",
            data=json_data,
            file_name=file_name,
            mime='application/json'
        )

        return len(data)  # Return the count of terms

    except Exception as e:
        st.error(f"An error occurred: {e}")
        return 0  # Return zero in case of error

# Function to create a backup of the JSON file
def backup_json(file_name):
    if os.path.exists(file_name):
        os.makedirs(backup_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file_name = os.path.join(backup_dir, f"backup_{timestamp}_{file_name}")
        shutil.copy(file_name, backup_file_name)
        st.success(f"Backup created: {backup_file_name}")
    else:
        st.warning("No file to backup.")

# Function to clear the content of the JSON file
def clear_json(file_name):
    if os.path.exists(file_name):
        backup_json(file_name)
        open(file_name, 'w').close()
        st.success(f"JSON file {file_name} has been cleared.")
    else:
        st.error(f"File {file_name} not found. Cannot clear a non-existent file.")

# Function to update the count of submissions
def update_submission_count(placeholder):
    if os.path.exists(file_name_terms_json):
        with open(file_name_terms_json, 'r', encoding='utf-8') as f:
            data = json.load(f)
            submission_count = len(data)
            placeholder.write(f"Number of Submissions: {submission_count}")
    else:
        placeholder.write("Number of Submissions: 0")

# Main function for Streamlit app
def page7_content():
    st.header("Conservation Biology Terms and Rankings")

    # Section for conservation biology terms
    st.subheader("Enter and Discuss Conservation Biology Terms")
    terms = ["Preservation ethic", "Resource conservation ethic", "Sustainable development", "Land ethic", "Ecosystem management"]
    data = {}

    for term in terms:
        st.write(f"### {term}")
        what = st.text_input(f"What is {term}?", key=f"{term}_what")
        pros = st.text_area(f"Pros of {term}:", key=f"{term}_pros")
        cons = st.text_area(f"Cons of {term}:", key=f"{term}_cons")

        if what or pros or cons:
            data[term] = {'what': what, 'pros': pros, 'cons': cons}

    if st.button("Save Submission"):
        save_to_json(data)
        st.rerun()  # Rerun to refresh immediately after submission

    # Display the current number of submissions
    submission_count_placeholder = st.empty()  # Placeholder for the count
    update_submission_count(submission_count_placeholder)

    st.subheader("Submissions")

    # Button to manually refresh JSON display
    if st.button("Refresh Submissions"):
        display_json(file_name_terms_json)

    # Button to clear and backup the JSON file
    if st.button("Clear Submissions"):
        clear_json(file_name_terms_json)
        st.rerun()  # Rerun to refresh immediately after clearing

# Run the app
if __name__ == "__main__":
    page7_content()
