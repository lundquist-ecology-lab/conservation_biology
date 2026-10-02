import streamlit as st
import pandas as pd
import os
import shutil
from datetime import datetime
import matplotlib.pyplot as plt
import time

from common.instructor import instructor_clear_button

# Define the file name to store rankings
rank_file = "environmental_issues_ranks.csv"

# Function to handle user rankings and update plot
def page0_content():
    st.header("Rank Important Environmental Issues")

    # Environmental issues to rank
    issues = [
        "Climate Change",
        "Biodiversity Loss",
        "Water/Food Scarcity",
        "Deforestation",
        "Pollution"
    ]

    # Get unique rankings from the user
    ranks = {}
    for issue in issues:
        rank = st.selectbox(f"Rank {issue} (1-5, unique)", options=[1, 2, 3, 4, 5], key=f"rank_{issue}")
        ranks[issue] = rank

    # Button to submit rankings
    if st.button("Submit Rankings"):
        if len(set(ranks.values())) < 5:
            st.error("All ranks must be unique!")
        else:
            save_ranks(ranks)
            st.success("Rankings submitted successfully!")
            time.sleep(2)
            st.rerun()  # Rerun to refresh the plot immediately after submission

    # Class results refresh on their own every 10 seconds without reloading the page
    live_results()

    # Clearing the shared class data is instructor-only
    if instructor_clear_button("Clear All Rankings", key="rankings"):
        clear_all_rankings()
        time.sleep(2)
        st.rerun()  # Rerun to refresh the page immediately after clearing


@st.fragment(run_every=10)
def live_results():
    if os.path.exists(rank_file):
        df = pd.read_csv(rank_file)
        st.write(f"Number of Submissions: {len(df)}")
        plot_ranks()
        st.write("Current Rankings:")
        st.dataframe(df)
    else:
        st.write("Number of Submissions: 0")
        st.info("No rankings have been submitted yet.")

# Function to save user rankings to CSV file
def save_ranks(ranks):
    # Convert rankings to DataFrame
    df = pd.DataFrame([ranks])

    # Check if the file exists and append or create a new file
    if os.path.exists(rank_file):
        df.to_csv(rank_file, mode='a', header=False, index=False)
    else:
        df.to_csv(rank_file, mode='w', header=True, index=False)

# Function to display the current rankings in the CSV file
def display_current_rankings():
    df = pd.read_csv(rank_file)
    st.write(df)

# Function to clear all rankings
def clear_all_rankings():
    if os.path.exists(rank_file):
        # Backup the CSV file before clearing
        backup_csv(rank_file)

        # Delete the CSV file to clear all rankings
        os.remove(rank_file)
        st.success("All rankings have been cleared.")
    else:
        st.error("No rankings to clear.")

# Function to create a backup of the CSV file
def backup_csv(file_name):
    if os.path.exists(file_name):
        # Create a backup file name with a timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file_name = f"backup_{timestamp}_{file_name}"

        # Copy the existing CSV to the backup file
        shutil.copy(file_name, backup_file_name)
        st.success(f"Backup created: {backup_file_name}")
    else:
        st.error("File not found. Cannot create a backup of a non-existent file.")

# Function to plot the average ranks and standard error
def plot_ranks():
    # Load the rankings from the CSV file
    df = pd.read_csv(rank_file)

    # Calculate the mean and standard error for each issue
    mean_ranks = df.mean()
    se_ranks = df.sem()

    # Plot the results with smaller fonts
    fig, ax = plt.subplots()
    ax.bar(mean_ranks.index, mean_ranks, yerr=se_ranks, capsize=5)
    ax.set_xlabel("Environmental Issues", fontsize=8)
    ax.set_ylabel("Average Rank", fontsize=8)
    ax.set_title("Average Rankings of Environmental Issues with SE", fontsize=8)
    ax.tick_params(axis='x', labelsize=5)
    ax.tick_params(axis='y', labelsize=5)

    st.pyplot(fig)


# Run the app
if __name__ == "__main__":
    page0_content()
