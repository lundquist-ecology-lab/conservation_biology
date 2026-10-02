import streamlit as st
import pandas as pd
import plotly.express as px


def page1_content():

    # IUCN Categories and their descriptions
    iucn_categories = {
        "Extinct (EX)": "No known living individuals remain",
        "Extinct in the Wild (EW)": "Known only to survive in captivity or as naturalized populations well outside their historic range",
        "Critically Endangered (CR)": "Extremely high risk of extinction in the wild",
        "Endangered (EN)": "Very high risk of extinction in the wild",
        "Vulnerable (VU)": "High risk of extinction in the wild",
        "Near Threatened (NT)": "Likely to become endangered in the near future",
        "Least Concern (LC)": "Lowest risk; does not qualify for a more at-risk category",
        "Data Deficient (DD)": "Not enough data to make an assessment of extinction risk"
    }

    # Title and Introduction
    st.title("IUCN Red List")
    st.markdown("""

            The International Union for Conservation of Nature (IUCN) Red List is the world's most comprehensive inventory of species' conservation status. 
            Founded in 1964, it acts as a critical indicator of the health of the world's biodiversity. The Red List uses a series of categories to rank 
            species from 'Extinct' to 'Least Concern', based on scientific assessments of population size, habitat, threats, and other factors. 
            It is widely recognized as the most authoritative guide for evaluating the global conservation status of plants and animals, and plays 
            a crucial role in guiding conservation action and policy worldwide.
            
        """)    
    
    st.markdown("### Threat Categories")
    for category, description in iucn_categories.items():
        st.markdown(f"**{category}**  \n{description}")
    
    st.markdown("""
        ### Explore Species Conservation Status
        
        Search for any species to view its current conservation status, population trends, 
        threats, and habitat information on the IUCN Red List website.
    """)

    col1, col2 = st.columns([3, 1])
    
    with col1:
        species_search = st.text_input("Enter species name (common or scientific):", 
                                    placeholder="e.g. Giant Panda or Ailuropoda melanoleuca")
    
    with col2:
        if st.button("Search IUCN", type="primary"):
            if species_search:
                search_url = f"https://www.iucnredlist.org/search?query={species_search}"
                # Create JavaScript to open in new tab
                js = f"""
                <script>
                    window.open('{search_url}', '_blank').focus();
                </script>
                """
                st.components.v1.html(js, height=0)
    
    st.markdown("""
        #### Search Tips:
        - Try both common names and scientific names
        - Be specific with species names (e.g., "Tiger" vs "Sumatran Tiger")
        - Check spelling if you don't get results
        
        *Note: You'll be taken directly to the IUCN Red List website in a new tab.*
    """)