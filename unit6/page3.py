import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
from PIL import Image
import requests
from io import BytesIO

def page3_content():
    
    st.title("Conservation Laws and Regulations")
    st.subheader("Local and International Legal Frameworks for Species Protection")

    # Introduction
    st.markdown("""
    This guide explores the complex network of laws and regulations that protect endangered species 
    and their habitats at both international and national levels. Understanding these legal frameworks 
    is crucial for effective conservation efforts.
    """)

    # Sidebar navigation
    page = st.sidebar.radio(
        "Navigate to:",
        ["International Laws", "National Laws", "Enforcement & Cases", "Success Stories"]
    )

    if page == "International Laws":
        show_international_laws()
    elif page == "National Laws":
        show_national_laws()
    elif page == "Enforcement & Cases":
        show_enforcement_cases()
    elif page == "Success Stories":
        show_success_stories()

def show_international_laws():
    st.header("International Conservation Laws")
    
    # Major international conventions
    conventions = {
        "CITES (Convention on International Trade in Endangered Species)": {
            "year": "1973",
            "description": "Regulates international trade in endangered species",
            "key_provisions": [
                "Appendix I: Species threatened with extinction",
                "Appendix II: Species not necessarily threatened but require trade control",
                "Appendix III: Species protected in at least one country"
            ],
            "example": "Successfully regulated trade in ivory, leading to elephant population recovery in some regions"
        },
        "Convention on Biological Diversity (CBD)": {
            "year": "1992",
            "description": "Comprehensive framework for sustainable development and biodiversity conservation",
            "key_provisions": [
                "Conservation of biological diversity",
                "Sustainable use of biodiversity components",
                "Fair sharing of benefits from genetic resources"
            ],
            "example": "Creation of protected areas networks in signatory countries"
        },
        "Ramsar Convention": {
            "year": "1971",
            "description": "Protection of wetlands of international importance",
            "key_provisions": [
                "Designation of wetlands for conservation",
                "Wise use of all wetlands",
                "International cooperation"
            ],
            "example": "Protection of the Pantanal wetlands in Brazil"
        }
    }
    
    for convention, details in conventions.items():
        with st.expander(f"{convention} ({details['year']})"):
            st.markdown(f"**Description:** {details['description']}")
            st.markdown("**Key Provisions:**")
            for provision in details['key_provisions']:
                st.markdown(f"- {provision}")
            st.markdown(f"**Real-world Example:** {details['example']}")

def show_national_laws():
    st.header("National Conservation Laws")
    
    # Select country to view
    country = st.selectbox(
        "Select a country to view its conservation laws:",
        ["United States", "Australia", "European Union"]
    )
    
    laws = {
        "United States": {
            "Endangered Species Act (ESA)": {
                "year": "1973",
                "description": "Comprehensive species and habitat protection law",
                "key_features": [
                    "Lists threatened and endangered species",
                    "Protects critical habitat",
                    "Requires recovery plans",
                    "Prohibits 'taking' of listed species"
                ],
                "example": "Recovery of the Bald Eagle population"
            },
            "Marine Mammal Protection Act": {
                "year": "1972",
                "description": "Protects all marine mammals in U.S. waters",
                "key_features": [
                    "Prohibits harassment and hunting",
                    "Regulates incidental capture",
                    "Establishes conservation programs"
                ],
                "example": "Protection of Hawaiian monk seals"
            }
        },
        "Australia": {
            "Environment Protection and Biodiversity Conservation Act": {
                "year": "1999",
                "description": "Primary environmental law for protecting biodiversity",
                "key_features": [
                    "Protects matters of national environmental significance",
                    "Regulates actions affecting protected species",
                    "Establishes protected areas"
                ],
                "example": "Protection of the Great Barrier Reef"
            }
        },
        "European Union": {
            "Birds Directive": {
                "year": "1979",
                "description": "Protection of all wild bird species in the EU",
                "key_features": [
                    "Creates Special Protection Areas",
                    "Regulates hunting",
                    "Protects habitats"
                ],
                "example": "Recovery of White-tailed Eagle populations"
            },
            "Habitats Directive": {
                "year": "1992",
                "description": "Conservation of natural habitats and wild fauna and flora",
                "key_features": [
                    "Establishes Natura 2000 network",
                    "Protects over 1000 species",
                    "Creates Special Areas of Conservation"
                ],
                "example": "Protection of wolf populations in Europe"
            }
        }
    }
    
    if country in laws:
        for law, details in laws[country].items():
            with st.expander(f"{law} ({details['year']})"):
                st.markdown(f"**Description:** {details['description']}")
                st.markdown("**Key Features:**")
                for feature in details['key_features']:
                    st.markdown(f"- {feature}")
                st.markdown(f"**Success Story:** {details['example']}")

def show_enforcement_cases():
    st.header("Enforcement Cases & Legal Precedents")
    
    cases = [
        {
            "name": "Tennessee Valley Authority v. Hill (1978)",
            "jurisdiction": "United States",
            "issue": "Snail darter protection under ESA vs. dam construction",
            "outcome": "Supreme Court ruled in favor of protecting the endangered snail darter, establishing the strength of the ESA",
            "impact": "Set precedent for prioritizing endangered species protection over development projects"
        },
        {
            "name": "Operation Chameleon (1995-2000)",
            "jurisdiction": "International",
            "issue": "Illegal wildlife trafficking network",
            "outcome": "Successful prosecution of major wildlife traffickers",
            "impact": "Demonstrated effectiveness of international law enforcement cooperation"
        },
        {
            "name": "European Commission v. Poland (Białowieża Forest)",
            "jurisdiction": "European Union",
            "issue": "Logging in protected old-growth forest",
            "outcome": "ECJ ruled against Poland's logging activities",
            "impact": "Strengthened protection of Natura 2000 sites"
        }
    ]
    
    for case in cases:
        with st.expander(case["name"]):
            cols = st.columns(2)
            with cols[0]:
                st.markdown(f"**Jurisdiction:** {case['jurisdiction']}")
                st.markdown(f"**Issue:** {case['issue']}")
            with cols[1]:
                st.markdown(f"**Outcome:** {case['outcome']}")
                st.markdown(f"**Impact:** {case['impact']}")

def load_image_from_url(url):
    try:
        response = requests.get(url)
        return Image.open(BytesIO(response.content))
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None
    
def show_success_stories():
    st.header("Conservation Success Stories Through Legal Protection")
    
    success_stories = {
        "American Bison Recovery": {
            "species": "American Bison",
            "image": "https://upload.wikimedia.org/wikipedia/commons/8/8d/American_bison_k5680-1.jpg",  # Example URL
            "image_caption": "American Bison in Yellowstone National Park",
            "laws_involved": ["Endangered Species Act", "State Wildlife Laws"],
            "population_change": "From fewer than 1,000 to over 500,000",
            "key_actions": [
                "Legal protection from hunting",
                "Habitat conservation requirements",
                "Reintroduction programs"
            ],
            "conservation_status": "Near Threatened"
        },
        "Gray Wolf Comeback": {
            "species": "Gray Wolf",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Eurasian_wolf_2.jpg/2560px-Eurasian_wolf_2.jpg",  # Example URL
            "image_caption": "Gray Wolf in Natural Habitat",
            "laws_involved": ["Endangered Species Act", "State Management Plans"],
            "population_change": "From almost extinct to over 6,000 in lower 48 states",
            "key_actions": [
                "Habitat protection",
                "Reintroduction programs",
                "Hunting restrictions"
            ],
            "conservation_status": "Least Concern"
        },
        "Humpback Whale Protection": {
            "species": "Humpback Whale",
            "image": "https://upload.wikimedia.org/wikipedia/commons/6/61/Humpback_Whale_underwater_shot.jpg",  # Example URL
            "image_caption": "Humpback Whale Breaching",
            "laws_involved": ["Marine Mammal Protection Act", "International Whaling Convention"],
            "population_change": "From 450 to over 25,000 in North Pacific",
            "key_actions": [
                "Commercial whaling ban",
                "Protected migration routes",
                "International cooperation"
            ],
            "conservation_status": "Least Concern"
        }
    }
    
    # Add image settings in sidebar
    st.sidebar.markdown("### Image Settings")
    image_width = st.sidebar.slider("Image Width", 200, 800, 400)
    
    for story, details in success_stories.items():
        with st.expander(story):
            # Create two columns - one for image and one for details
            col1, col2 = st.columns([1, 1])
            
            with col1:
                # Display image with caption and error handling
                try:
                    st.image(
                        details["image"],
                        caption=details["image_caption"],
                        width=image_width,
                        use_column_width=False
                    )
                except Exception as e:
                    st.error(f"Error loading image: {e}")
                    st.image("/api/placeholder/400/300", caption="Image unavailable")
                
            with col2:
                # Display species information
                st.markdown(f"### {details['species']}")
                st.markdown(f"**Conservation Status:** {details['conservation_status']}")
                
                # Create a visual separation
                st.markdown("---")
                
                # Display laws and actions
                st.markdown("**Laws Involved:**")
                for law in details['laws_involved']:
                    st.markdown(f"- {law}")
                
                st.markdown("**Key Legal Actions:**")
                for action in details['key_actions']:
                    st.markdown(f"- {action}")            
            
            # Add source and reference information
            st.markdown("---")
            st.markdown("**Image Source:**")
            st.markdown(f"[Link to original image]({details['image']})")
