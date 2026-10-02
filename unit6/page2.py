import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from PIL import Image

def page2_content():    
    st.title("Conservation Priorities")
    
    # Introduction
    st.markdown("""
    Setting conservation priorities are crucial for effectively allocating limited resources 
    to protect biodiversity and ecosystems. However, there are many different approaches to 
    determine conservation priorities.
    """)

    # Sidebar for navigation
    page = st.sidebar.radio(
        "Navigate to:",
        ["Key Approaches", "Criteria & Metrics", "Priority Setting Tools", "Case Studies"]
    )

    if page == "Key Approaches":
        show_key_approaches()
    elif page == "Criteria & Metrics":
        show_criteria_metrics()
    elif page == "Priority Setting Tools":
        show_priority_tools()
    elif page == "Case Studies":
        show_case_studies()

def show_key_approaches():
    st.header("Key Approaches to Conservation Prioritization")
    
    approaches = {
        "Species-based Approach": {
            "description": "Focuses on protecting individual species, particularly those that are endangered or keystone species.",
            "pros": ["Direct impact on threatened species", "Clear metrics for success", "Public appeal"],
            "cons": ["May miss ecosystem-level issues", "Resource intensive", "Limited scope"]
        },
        "Ecosystem-based Approach": {
            "description": "Prioritizes protection of entire ecosystems and ecological processes.",
            "pros": ["Protects multiple species", "Maintains ecological processes", "Cost-effective"],
            "cons": ["Complex to implement", "Harder to measure success", "May miss specific species needs"]
        },
        "Hotspot Approach": {
            "description": "Focuses on areas with high biodiversity and significant threats.",
            "pros": ["Maximizes biodiversity protection", "Clear geographical focus", "Evidence-based"],
            "cons": ["May overlook less diverse but important areas", "Requires extensive data", "Can be politically challenging"]
        },
        "Systematic Conservation Planning": {
            "description": "Uses systematic, data-driven methods to identify priority areas and actions.",
            "pros": ["Comprehensive", "Scientifically robust", "Efficient resource use"],
            "cons": ["Data-intensive", "Technical expertise required", "Time-consuming"]
        }
    }
    
    for approach, details in approaches.items():
        with st.expander(approach):
            st.markdown(f"**Description:** {details['description']}")
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Advantages:**")
                for pro in details['pros']:
                    st.markdown(f"- {pro}")
            
            with col2:
                st.markdown("**Disadvantages:**")
                for con in details['cons']:
                    st.markdown(f"- {con}")

def show_criteria_metrics():
    st.header("Criteria & Metrics for Priority Setting")
    
    # Create tabs for different criteria categories
    tab1, tab2, tab3 = st.tabs(["Biological Criteria", "Socioeconomic Criteria", "Feasibility Criteria"])
    
    with tab1:
        st.subheader("Biological Criteria")
        bio_criteria = pd.DataFrame({
            'Criterion': ['Species Richness', 'Endemism', 'Threatened Species', 'Ecosystem Services'],
            'Description': [
                'Number of different species in an area',
                'Presence of species found nowhere else',
                'Number of endangered or threatened species',
                'Value of ecosystem functions and services'
            ],
            'Measurement': [
                'Species counts, diversity indices',
                'Endemic species count, range restriction',
                'IUCN Red List categories',
                'Economic valuation, service quantification'
            ]
        })
        st.dataframe(bio_criteria, hide_index=True)

    with tab2:
        st.subheader("Socioeconomic Criteria")
        socio_criteria = pd.DataFrame({
            'Criterion': ['Local Community Impact', 'Economic Value', 'Cultural Significance', 'Development Pressure'],
            'Description': [
                'Effects on local communities and livelihoods',
                'Direct and indirect economic benefits',
                'Cultural and historical importance',
                'Threats from development activities'
            ],
            'Measurement': [
                'Livelihood assessments, social surveys',
                'Cost-benefit analysis, ecosystem service valuation',
                'Cultural mapping, stakeholder consultations',
                'Development plans, land use change analysis'
            ]
        })
        st.dataframe(socio_criteria, hide_index=True)

    with tab3:
        st.subheader("Feasibility Criteria")
        feasibility_criteria = pd.DataFrame({
            'Criterion': ['Cost', 'Political Support', 'Technical Feasibility', 'Time Frame'],
            'Description': [
                'Financial resources required',
                'Level of government and stakeholder support',
                'Availability of necessary expertise and technology',
                'Time required for implementation'
            ],
            'Measurement': [
                'Budget estimates, cost-effectiveness analysis',
                'Policy analysis, stakeholder mapping',
                'Capacity assessments, resource evaluation',
                'Project timeline analysis, milestone planning'
            ]
        })
        st.dataframe(feasibility_criteria, hide_index=True)

def show_priority_tools():
    st.header("Priority Setting Tools")
    
    tools = {
        "Marxan": {
            "description": "Software for systematic conservation planning that helps identify sets of priority areas.",
            "use_cases": ["Reserve design", "Conservation network planning", "Cost-effective conservation solutions"]
        },
        "Zonation": {
            "description": "Spatial conservation prioritization framework for large-scale conservation planning.",
            "use_cases": ["Landscape prioritization", "Connectivity analysis", "Species distribution modeling"]
        },
        "InVEST": {
            "description": "Suite of models for mapping and valuing ecosystem services.",
            "use_cases": ["Ecosystem service assessment", "Natural capital valuation", "Impact assessment"]
        },
        "Key Biodiversity Areas (KBA)": {
            "description": "Standardized approach to identifying globally important sites for biodiversity conservation.",
            "use_cases": ["Biodiversity importance assessment", "Protected area planning", "International priority setting"]
        }
    }
    
    cols = st.columns(2)
    for idx, (tool, info) in enumerate(tools.items()):
        with cols[idx % 2]:
            st.markdown(f"### {tool}")
            st.markdown(f"**Description:** {info['description']}")
            st.markdown("**Key Use Cases:**")
            for case in info['use_cases']:
                st.markdown(f"- {case}")

def show_case_studies():
    st.header("Case Studies in Conservation Priority Setting")
    
    case_studies = [
        {
            "title": "Amazon Protected Areas Program",
            "approach": "Systematic Conservation Planning",
            "outcomes": ["Created network of protected areas", "Increased indigenous land rights", "Reduced deforestation"],
            "lessons": "Integration of multiple stakeholders and criteria leads to more effective conservation outcomes."
        },
        {
            "title": "Madagascar Biodiversity Conservation",
            "approach": "Hotspot Approach",
            "outcomes": ["Identified priority areas for endemic species", "Established new protected areas", "Enhanced local capacity"],
            "lessons": "Combining biological importance with feasibility criteria is crucial for successful implementation."
        },
        {
            "title": "Great Barrier Reef Marine Park Zoning",
            "approach": "Ecosystem-based Approach",
            "outcomes": ["Increased no-take zones", "Improved reef resilience", "Better stakeholder engagement"],
            "lessons": "Adaptive management and stakeholder involvement are key to successful marine conservation."
        }
    ]
    
    for study in case_studies:
        with st.expander(study["title"]):
            st.markdown(f"**Approach Used:** {study['approach']}")
            st.markdown("**Key Outcomes:**")
            for outcome in study["outcomes"]:
                st.markdown(f"- {outcome}")
            st.markdown(f"**Key Lessons:** {study['lessons']}")