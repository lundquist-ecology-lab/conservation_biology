import streamlit as st
import pandas as pd

def page0_content():
    
    st.title("Establishing New Populations")
    st.subheader("Understanding Different Approaches and Considerations")

    # Introduction
    st.markdown("""
    Conservation biologists often need to establish new populations of species to ensure their survival. 
    This can be done through various approaches, each with its own challenges and considerations.
    """)

    # Main approaches section
    st.header("Main Approaches to Population Establishment")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### Reintroduction
        Returning a species to an area where it previously existed but has been extirpated.
        
        **Key Points:**
        - Requires historical evidence of previous occurrence
        - Habitat must still be suitable
        - Original causes of extinction must be addressed
        - Local community support is crucial
        """)

    with col2:
        st.markdown("""
        ### Reinforcement
        Adding individuals to an existing population to increase population size or genetic diversity.
        
        **Key Points:**
        - Also known as supplementation
        - Helps prevent genetic bottlenecks
        - Can rescue declining populations
        - Risk of disease introduction
        """)

    with col3:
        st.markdown("""
        ### Introduction
        Moving a species to an area outside its historical range.
        
        **Key Points:**
        - Used when historical range is no longer suitable
        - Higher risk due to unknown interactions
        - Last resort conservation method
        - Careful assessment needed
        """)

    # IUCN Guidelines
    st.header("IUCN Guidelines for Reintroductions")
    
    with st.expander("View IUCN Considerations"):
        st.markdown("""
        ### 1. Biological Feasibility
        - Habitat requirements
        - Available suitable release sites
        - Sufficient founder population
        - Genetic considerations
        
        ### 2. Social Feasibility
        - Local community support
        - Political and stakeholder support
        - Legal requirements
        - Long-term financial support
        
        ### 3. Risk Assessment
        - Impact on source populations
        - Disease risk
        - Ecological impact on other species
        - Genetic risks
        
        ### 4. Implementation Strategy
        - Release strategies
        - Monitoring protocols
        - Exit strategy if needed
        - Documentation requirements
        """)

    # Challenges and Solutions
    st.header("Common Challenges and Solutions")
    
    challenges_df = pd.DataFrame({
        'Challenge': [
            'Habitat Quality',
            'Genetic Diversity',
            'Disease Risk',
            'Human Conflict',
            'Climate Change'
        ],
        'Description': [
            'Ensuring habitat meets all species requirements',
            'Maintaining adequate genetic diversity in new population',
            'Preventing disease transmission between populations',
            'Managing human-wildlife conflict in release areas',
            'Accounting for changing environmental conditions'
        ],
        'Potential Solutions': [
            'Habitat restoration, protected area establishment',
            'Careful selection of founder individuals, genetic monitoring',
            'Health screening, quarantine protocols',
            'Community engagement, compensation schemes',
            'Climate-smart conservation planning, assisted migration'
        ]
    })
    
    st.dataframe(challenges_df, use_container_width=True)

    # Case Studies Section
    st.header("Case Studies")
    
    case_study = st.selectbox(
        "Select a case study to learn more:",
        ["California Condor Reintroduction",
         "European Bison Reintroduction",
         "Wolf Reintroduction to Yellowstone"]
    )

    # Image URLs for each case study
    images = {
        "California Condor Reintroduction": "https://upload.wikimedia.org/wikipedia/commons/1/11/California-condor-gymnogyps-californianus-078_%2821196759264%29.jpg",
        "European Bison Reintroduction": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/European_bison_%28Bison_bonasus%29_male_Bia%C5%82owieza.jpg/2560px-European_bison_%28Bison_bonasus%29_male_Bia%C5%82owieza.jpg",
        "Wolf Reintroduction to Yellowstone": "https://upload.wikimedia.org/wikipedia/commons/0/00/Yellowstone-wolf-17120.jpg"
    }

    case_studies = {
        "California Condor Reintroduction": """
        - Started in 1992
        - Last wild condors captured in 1987
        - Successful captive breeding program
        - Current population >400 birds
        - Ongoing challenges with lead poisoning
        """,
        
        "European Bison Reintroduction": """
        - Extinct in wild by 1927
        - Survived only in zoos
        - Reintroduced to Białowieża Forest
        - Current population >7000
        - Example of successful reintroduction
        """,
        
        "Wolf Reintroduction to Yellowstone": """
        - Reintroduced in 1995-1996
        - 41 wolves initially released
        - Demonstrated trophic cascade effects
        - Population stabilized around 100 wolves
        - Significant ecosystem impacts
        """
    }

    # Create two columns for image and text
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.image(images[case_study], caption=f"{case_study} Species", use_column_width=True)
    
    with col2:
        st.markdown(case_studies[case_study])