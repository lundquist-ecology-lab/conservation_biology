import streamlit as st

def page2_content():
    st.title("Design Your Protected Area")
    st.markdown("---")

    st.markdown("""
    ### Introduction
    In this activity, you will create and plan your own protected area. Think creatively about how to balance conservation goals with practical management challenges.
    """)

    tabs = st.tabs([
        "Step 1: Site Selection",
        "Step 2: Ecosystem Analysis",
        "Step 3: Design Elements",
        "Step 4: Management Planning",
        "Step 5: Stakeholder Engagement",
        "Final Project"
    ])

    with tabs[0]:
        st.header("Step 1: Site Selection")
        st.markdown("""
        ### Choose Your Location
        Select a region for your protected area. 
        
        Consider:

        **Landscape Features:**
        - What ecosystem types are present?
        - Are there unique geographical features?
        - What are the climate conditions?

        **Conservation Value:**
        - Are there endangered species?
        - What critical habitats exist?
        - Are there important ecological processes?

        **Site Description**
        Write a brief description of your chosen site including:
        1. Geographic location and size
        2. Main ecosystems present
        3. Key species to protect
        4. Unique features or characteristics
        """)

    with tabs[1]:
        st.header("Step 2: Ecosystem Analysis")
        st.markdown("""
        ### Analyze Your Ecosystems
        Map out the ecological components of your protected area.

        **Ecosystem Mapping**
        Create a rough sketch showing:
        1. Major habitat types
        2. Water sources
        3. Critical wildlife areas
        4. Existing human activities

        **Species Assessment**
        List:
        1. Flagship species
        2. Keystone species
        3. Endemic species
        4. Migratory species

        **Questions to Consider:**
        - How do different species use the landscape?
        - What are the seasonal patterns?
        - Where are the ecological hotspots?
        """)

    with tabs[2]:
        st.header("Step 3: Design Elements")
        st.markdown("""
        ### Plan Your Protected Area Design

        **Zoning Plan**
        Define different management zones:
        1. Core protection zones
        2. Buffer zones
        3. Sustainable use zones
        4. Tourism areas

        **Connectivity Planning**
        Design wildlife corridors considering:
        - Migration routes
        - Habitat connections
        - Seasonal movements
        - Buffer requirements

        **Design Principles to Apply:**
        - SLOSS (Single Large or Several Small)
        - Edge effects
        - Island biogeography
        - Corridor design
        """)

    with tabs[3]:
        st.header("Step 4: Management Planning")
        st.markdown("""
        ### Develop Management Strategies

        **Threat Assessment**
        Identify potential threats:
        - Poaching risks
        - Human-wildlife conflict
        - Habitat degradation
        - Climate change impacts

        **Management Solutions**
        Develop strategies for:
        1. Anti-poaching
        2. Conflict mitigation
        3. Habitat restoration
        4. Tourism management

        **Resource Planning**
        Consider needs for:
        - Staff and equipment
        - Infrastructure
        - Monitoring systems
        - Emergency response
        """)

    with tabs[4]:
        st.header("Step 5: Stakeholder Engagement")
        st.markdown("""
        ### Plan Community Integration

        **Stakeholder Mapping**
        Identify key stakeholders:
        - Local communities
        - Indigenous groups
        - Government agencies
        - Conservation organizations
        - Tourism operators

        **Communication Strategy**
        Develop plans for:
        - Community outreach
        - Visitor education
        - Stakeholder coordination
        - Conflict resolution
        """)

    with tabs[5]:
        st.header("Protected Area Proposal")
        st.markdown("""
        ### Compile Your Protected Area Plan

        **Project Components:**
        1. Executive Summary
            - Site description
            - Conservation goals
            - Key features

        2. Technical Details
            - Maps and zones
            - Management plans
            - Resource needs

        3. Implementation Strategy
            - Timeline
            - Budget
            - Staffing plan
            - Monitoring approach

        4. Impact Assessment
            - Conservation benefits
            - Community impacts
            - Economic considerations
            - Long-term sustainability

        **Creative Elements to Include:**
        - Visual representations
        - Innovation in design
        - Creative solutions
        - Unique features

        **Evaluation Criteria:**
        - Ecological soundness
        - Management feasibility
        - Stakeholder integration
        - Innovation
        - Sustainability
        """)