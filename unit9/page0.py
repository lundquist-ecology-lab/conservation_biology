import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

def page0_content():    
    st.title("Ecological Restoration in Conservation Biology")

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    section = st.sidebar.radio(
        "Go to",
        ["Ecological Succession", "Active vs. Passive Management", "Terrestrial Restoration", "Stream Restoration", "Chesapeake Bay Restoration"]
    )

    if section == "Ecological Succession":
        show_succession()
        
    elif section == "Active vs. Passive Management":
        show_management()
    elif section == "Terrestrial Restoration":
        show_terrestrial()
    elif section == "Stream Restoration":
        show_stream()
    else:
        show_chesapeake()

def show_succession():
    st.header("Ecological Succession")
    
    # Interactive succession visualization
    st.subheader("Stages of Secondary Succession")
    
    # Create sample data for secondary succession visualization
    succession_data = pd.DataFrame({
        'Stage': ['Disturbance', 'Pioneer Species', 'Grasses & Herbs', 'Shrubs', 'Pioneer Trees', 'Mature Forest'],
        'Time (years)': [0, 1, 3, 10, 20, 50],
        'Biodiversity': [10, 20, 40, 60, 80, 100],
        'Soil Quality Index': [50, 60, 70, 80, 90, 100]
    })
    
    # Interactive chart
    metric = st.selectbox("Select metric to visualize", ['Biodiversity', 'Soil Quality Index'])
    
    chart = alt.Chart(succession_data).mark_line(point=True).encode(
        x='Time (years)',
        y=metric,
        tooltip=['Stage', 'Time (years)', metric]
    ).properties(height=400)
    
    st.altair_chart(chart, use_container_width=True)
    
    st.write("""
    **Secondary succession** occurs in ecosystems where a disturbance (e.g., fire, farming, or logging) has cleared vegetation but left the soil intact. 
    The stages include:
    - **Pioneer species**: Fast-growing plants like grasses and herbs.
    - **Intermediate species**: Shrubs and young trees establish.
    - **Climax community**: Stable ecosystems with mature vegetation and high biodiversity.
    
    Secondary succession often happens faster than primary succession due to the presence of soil and seed banks.
    """)
    
    st.image("https://openstax.org/apps/archive/20241024.164013/resources/2d866912364c68b0717cef0decd46aad4771eaac", 
             caption="Secondary Succession (OpenStax)",
             use_column_width=True)

def show_management():
    st.header("Active vs. Passive Management in Succession")
    st.write("""
    Management strategies influence the trajectory of succession and ecosystem recovery. Two common approaches are:

    **Active Management**
    - Direct interventions to guide succession or address invasive species.
    - **Examples**:
      - Replanting native species in post-disturbance areas.
      - Controlling invasive species like Phragmites or kudzu.
      - Soil stabilization through erosion control.
    - **Pros**: Faster recovery, targeted outcomes, control over species composition.
    - **Cons**: Labor-intensive, costly, potential unintended consequences.

    **Passive Management**
    - Allowing natural processes to drive recovery with minimal interference.
    - **Examples**:
      - Leaving abandoned farmland to regrow naturally.
      - Allowing wetlands to recover after pollution reductions.
    - **Pros**: Cost-effective, promotes natural biodiversity.
    - **Cons**: Slower recovery, less control over invasive species.

    **Balancing Active and Passive Management**
    - Many restoration projects combine both strategies, using active management to address immediate threats (e.g., invasives) and passive methods for long-term recovery.
    """)

def show_terrestrial():
    st.header("Terrestrial Ecosystem Restoration")
    
    st.subheader("Key Restoration Strategies")
    st.write("""
    1. **Native Species Reintroduction**
        - Carefully selected species based on historical records
        - Consideration of current environmental conditions
        - Monitoring of establishment success
    
    2. **Soil Rehabilitation**
        - Organic matter addition
        - pH adjustment
        - Erosion control measures
    
    3. **Invasive Species Management**
        - Regular monitoring
        - Multiple control methods
        - Prevention strategies
    """)
    

def show_stream():
    st.header("Stream Ecosystem Restoration")
    
    st.subheader("Common Stream Restoration Techniques")
    
    # Interactive demonstration of stream restoration
    technique = st.selectbox(
        "Select restoration technique to learn more:",
        ["Channel Reconstruction", "Riparian Buffer Enhancement", "In-stream Habitat Structures", "Fish Passage"]
    )
    
    techniques = {
        "Channel Reconstruction": """
        Involves reshaping the stream channel to restore natural meanders and flow patterns.
        Benefits include:
        - Reduced erosion
        - Improved habitat diversity
        - Better flood control
        - Enhanced sediment transport
        """,
        
        "Riparian Buffer Enhancement": """
        Focuses on restoring vegetation along stream banks.
        Key aspects include:
        - Temperature regulation
        - Nutrient filtration
        - Bank stabilization
        - Wildlife corridors
        """,
        
        "In-stream Habitat Structures": """
        Addition of physical structures to improve habitat quality.
        Examples include:
        - Root wads
        - Boulder clusters
        - Woody debris
        - Artificial riffles
        """,
        
        "Fish Passage": """
        Modifications to allow fish movement through barriers.
        Approaches include:
        - Fish ladders
        - Dam removal
        - Culvert modification
        - Bypass channels
        """
    }
    
    st.write(techniques[technique])

def show_chesapeake():
    st.header("Chesapeake Bay Restoration")
    
    st.subheader("Restoration Progress (2000-2023)")
    
    # Updated historical data for Chesapeake Bay indicators
    bay_data = pd.DataFrame({
        'Year': [2000, 2005, 2010, 2015, 2020, 2023],
        'Water Quality Index': [28, 27, 31, 34, 32, 32],  # Based on Chesapeake Bay Foundation's State of the Bay Report
        'Underwater Grass Acres': [85_252, 89_659, 79_664, 91_621, 62_169, 82_937],  # Submerged aquatic vegetation
        'Oyster Population (%)': [1, 2, 9, 12, 15, 20]  # Percentage of historic population levels
    })
    
    # Add explanatory text
    st.write("""
    The Chesapeake Bay has experienced varied progress in restoration efforts since 2000. Key indicators help us track the bay's health:
    - **Water Quality Index**: Measures factors like dissolved oxygen, water clarity, and chlorophyll a. Scores are based on a 100-point scale; for instance, the 2022 score was 32, indicating significant room for improvement. :contentReference[oaicite:0]{index=0}
    - **Underwater Grass Acres**: Indicates habitat quality and water clarity. In 2023, underwater grasses expanded to an estimated 82,937 acres, a 7% increase over 2022, reaching the seventh-highest level in 40 years of monitoring. :contentReference[oaicite:1]{index=1}
    - **Oyster Population**: Measured as a percentage of historic population levels. Restoration projects have increased oyster populations to approximately 20% of historic levels.
    """)
    
    st.image("https://openstax.org/apps/archive/20241024.164013/resources/8343a70038d91c7c281f278878f9bb2d58c9873a",
             caption="Chesapeake Bay watershed (OpenStax)",
             use_column_width=True)
    
    st.write("""
    Learn more about restoration efforts on the [Chesapeake Bay Foundation website](https://www.cbf.org/about-cbf/our-mission/restore/index.html).
    """)
    
    # Interactive visualization
    metric = st.selectbox(
        "Select indicator to visualize",
        ['Water Quality Index', 'Underwater Grass Acres', 'Oyster Population (%)']
    )
    
    chart = alt.Chart(bay_data).mark_line(point=True).encode(
        x=alt.X('Year', scale=alt.Scale(domain=[2000, 2023])),
        y=metric,
        tooltip=['Year', metric]
    ).properties(height=400)
    
    st.altair_chart(chart, use_container_width=True)
    
    # Add detailed restoration information
    st.subheader("Major Restoration Milestones")
    st.write("""
    **2000-2010: Early Progress**
    - Establishment of pollution reduction goals.
    - Implementation of agricultural best practices.
    - Initiation of large-scale oyster restoration projects.
    
    **2010-2020: Chesapeake Bay TMDL**
    - Implementation of the Total Maximum Daily Load (TMDL) "pollution diet".
    - Expansion of watershed implementation plans.
    - Acceleration of wetland restoration.
    - Creation of tributary-specific oyster restoration plans.
    
    **2020-Present: Current Initiatives**
    - Enhanced focus on climate change resilience.
    - Expansion of living shoreline projects.
    - Increased emphasis on environmental justice.
    - Implementation of adaptive management strategies.
    """)
    
    # Add specific restoration projects
    st.subheader("Key Restoration Projects")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("""
        **Habitat Restoration**
        - **Oyster Reef Restoration**: Significant progress has been made, with restoration efforts completed in eight of the ten targeted tributaries as of 2023.
        - **Submerged Aquatic Vegetation (SAV) Restoration**: Underwater grasses expanded to an estimated 82,937 acres in 2023, marking a 7% increase over 2022 and achieving the seventh-highest level in 40 years of monitoring. :contentReference[oaicite:2]{index=2}
        """)
    
    with col2:
        st.write("""
        **Water Quality Improvements**
        - **Pollution Reduction**: Implementation of the Chesapeake Bay TMDL has led to reductions in nitrogen and phosphorus levels.
        - **Stormwater Management**: Urban stormwater retrofits have treated thousands of acres to reduce runoff.
        """)
    
    # Add challenges section
    st.subheader("Ongoing Challenges")
    st.write("""
    Despite progress, the Chesapeake Bay faces continuing challenges:
    1. **Climate Change Impacts**
       - Rising water temperatures.
       - Increased storm intensity.
       - Sea-level rise affecting wetlands.
    
    2. **Population Growth Pressures**
       - Expanding urban development.
       - Increased nutrient runoff.
       - Habitat fragmentation.
    
    3. **Agricultural Runoff**
       - Nutrient management compliance.
       - Soil conservation practices.
       - Cost of implementation.
    """)