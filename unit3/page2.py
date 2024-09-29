import streamlit as st
import matplotlib.pyplot as plt
import sqlite3

# Function to connect to the SQLite database (or create it if it doesn't exist)
def get_database_connection():
    conn = sqlite3.connect('action_counts.db')
    return conn

# Function to initialize the database table if it doesn't exist
def init_db():
    conn = get_database_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS actions
                 (action TEXT PRIMARY KEY, count INTEGER)''')
    # Initialize with default actions if empty
    c.execute('SELECT COUNT(*) FROM actions')
    if c.fetchone()[0] == 0:
        default_actions = [
            ("Reducing Waste and Pollution", 0),
            ("Protecting Endangered Species", 0),
            ("Promoting Sustainable Agriculture", 0),
            ("Advocating for Climate Action", 0),
            ("Preserving Ecosystems", 0),
            ("Supporting Environmental Education", 0),
        ]
        c.executemany('INSERT INTO actions (action, count) VALUES (?, ?)', default_actions)
        conn.commit()
    conn.close()

# Function to fetch action counts from the database
def get_action_counts():
    conn = get_database_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM actions')
    action_counts = {row[0]: row[1] for row in c.fetchall()}
    conn.close()
    return action_counts

# Function to update action counts in the database
def update_action_counts(action):
    conn = get_database_connection()
    c = conn.cursor()
    c.execute('UPDATE actions SET count = count + 1 WHERE action = ?', (action,))
    conn.commit()
    conn.close()

# Function to reset action counts in the database (clearing the plot)
def reset_action_counts():
    conn = get_database_connection()
    c = conn.cursor()
    c.execute('UPDATE actions SET count = 0')  # Reset all counts to 0
    conn.commit()
    conn.close()

# Initialize the database
init_db()

def page2_content():
    st.header("Environmental Ethics and Human Stewardship")
    st.write(
        """
        Environmental ethics explores the moral relationship between humans and the natural world. 
        It raises questions about how we should value nature, what responsibilities we have to other 
        species, and how we can balance human needs with the health of our planet.
        
        As stewards of the natural world, humans play a critical role in protecting and preserving the environment. 
        But what does it mean to be a steward? How should we act, and what principles should guide our behavior?
        """
    )

    st.subheader("Reflect on Different Ethical Perspectives")
    st.write("Choose a perspective below and consider its implications for environmental stewardship:")

    ethical_perspective = st.selectbox(
        "Select an Ethical Perspective:",
        ["Anthropocentrism", "Biocentrism", "Ecocentrism", "Deep Ecology"]
    )

    if ethical_perspective == "Anthropocentrism":
        st.write(
            """
            **Anthropocentrism** places human needs and interests at the center of ethical considerations. 
            It suggests that the environment should be protected primarily because it benefits humans. 
            Consider how this view might influence decisions about natural resource use or conservation.
            """
        )
    elif ethical_perspective == "Biocentrism":
        st.write(
            """
            **Biocentrism** argues that all living beings have intrinsic value, regardless of their utility to humans. 
            This perspective promotes respect for all forms of life and encourages a more holistic approach to environmental protection.
            Reflect on how this view might change our priorities in environmental policy.
            """
        )
    elif ethical_perspective == "Ecocentrism":
        st.write(
            """
            **Ecocentrism** expands the moral consideration to entire ecosystems, including non-living elements. 
            It emphasizes the interconnectedness of all components of the environment and suggests that we should prioritize the health of the whole ecosystem.
            Think about how this perspective might influence our actions in dealing with climate change or habitat destruction.
            """
        )
    else:
        st.write(
            """
            **Deep Ecology** promotes the inherent worth of all living beings and advocates for a radical shift in human behavior 
            to maintain the ecological balance of the planet. It calls for a profound transformation in our relationship with nature, 
            valuing simplicity and harmony with natural systems over consumption and economic growth.
            Consider what changes in lifestyle and policy would be needed to align with this perspective.
            """
        )

    st.subheader("Interactive Exercise")
    st.write("Select your top action as a steward of the environment:")

    # Fetch the latest counts from the database
    action_counts = get_action_counts()

    # Dropdown to select top action
    top_action = st.selectbox(
        "Choose your top action:",
        list(action_counts.keys())
    )

    # Button to add the selected action to the plot data
    if st.button("Add to Graph"):
        update_action_counts(top_action)
        st.success(f"Added {top_action} to the graph.")
        action_counts = get_action_counts()  # Refresh the counts after update

    # Button to refresh the graph
    if st.button("Refresh Graph"):
        action_counts = get_action_counts()  # Refresh counts from the database
        st.success("Graph refreshed with the latest data.")

    # Button to clear the plot (reset the database)
    if st.button("Clear Plot"):
        reset_action_counts()  # Reset all counts to 0
        action_counts = get_action_counts()  # Refresh counts
        st.warning("Plot cleared. All action counts reset to 0.")

    # Prepare the data for plotting
    actions = list(action_counts.keys())
    counts = list(action_counts.values())

    # Define a list of colors for the bars
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

    col1, col2 = st.columns([3, 1])  # Create two equal-sized columns

    with col1:
        # Plot the data
        fig, ax = plt.subplots()
        ax.bar(actions, counts, color=colors)
        ax.set_xlabel('Actions', fontsize=10)
        ax.set_ylabel('Count', fontsize=10)
        ax.set_title('Top Stewardship Actions', fontsize=12)

        # Rotate x-axis labels, set smaller font size, and ensure y values are whole numbers
        ax.set_xticklabels(actions, rotation=90, fontsize=8)
        ax.set_yticks(range(0, max(counts) + 1))  # Ensuring y values are whole numbers
        ax.tick_params(axis='y', labelsize=8)

        # Display the plot
        st.pyplot(fig)
