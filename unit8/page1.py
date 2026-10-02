import streamlit as st

def page1_content():
    st.title("Protected Area Management Challenges")
    st.markdown("---")

    tabs = st.tabs([
        "Poaching", 
        "Trophy Hunting",
        "Human-Wildlife Conflict",
        "Habitat Degradation",
        "Climate Change",
        "Funding"
    ])

    # Tab 1: Poaching
    with tabs[0]:
        st.header("Poaching Management")
        
        st.markdown("""
        ### Introduction to Poaching
        Poaching represents one of the most significant challenges in protected area management, threatening biodiversity and ecosystem stability. Success in anti-poaching requires addressing multiple interconnected factors simultaneously.

        ### Key Risk Factors
        - Patrol Coverage and Effectiveness
        - Boundary Security and Access Control
        - Local Poverty and Economic Conditions
        - Market Demand for Wildlife Products
        - International Trade Networks

        ### Anti-Poaching Strategies
        Modern anti-poaching efforts combine traditional methods with new technologies and community engagement. Effective programs typically integrate multiple approaches:

        - Ground Patrols and Surveillance
        - Technology Integration (drones, cameras, GPS)
        - Community Intelligence Networks
        - International Cooperation

        ### Community Engagement
        Local community support is crucial for successful anti-poaching efforts. Key aspects include:
        
        - Alternative Livelihood Programs
        - Information Sharing Networks
        - Education and Awareness
        - Benefit-Sharing Mechanisms
        """)

    # Tab 2: Trophy Hunting
    with tabs[1]:
        st.header("Trophy Hunting Management")
        
        st.markdown("""
        ### Overview
        Trophy hunting presents a complex intersection of conservation, economics, and ethics. Proper management requires careful balance of multiple objectives.

        ### Economic Aspects
        - Permit and Quota Systems
        - Revenue Distribution Models
        - Community Benefit Sharing
        - Infrastructure Development

        ### Population Management
        Sustainable trophy hunting depends on scientific management of wildlife populations:

        - Population Monitoring
        - Breeding Patterns and Social Structure
        - Habitat Requirements
        - Sustainable Quota Setting

        ### Management Considerations
        Key factors for successful trophy hunting programs:
        
        - Scientific Monitoring Systems
        - Community Participation
        - Transparent Operations
        - Conservation Reinvestment
        """)

    # Tab 3: Human-Wildlife Conflict
    with tabs[2]:
        st.header("Human-Wildlife Conflict Management")
        
        st.markdown("""
        ### Understanding the Conflict
        Human-wildlife conflict occurs at the interface between protected areas and human settlements, creating complex management challenges that affect both wildlife and local communities.

        ### Major Conflict Types
        - Crop Damage and Agricultural Losses
        - Livestock Predation
        - Infrastructure Damage
        - Human Safety Threats

        ### Impact Assessment
        Common impacts of human-wildlife conflict:

        - Economic Losses
        - Food Security Issues
        - Retaliatory Killings
        - Social and Cultural Disruption

        ### Mitigation Approaches
        Effective conflict management requires multiple strategies:

        - Physical Barriers (fencing, trenches)
        - Early Warning Systems
        - Compensation Programs
        - Alternative Livelihoods
        """)

    # Tab 4: Habitat Degradation
    with tabs[3]:
        st.header("Habitat Degradation Assessment")
        
        st.markdown("""
        ### Understanding Degradation
        Habitat degradation occurs through multiple pathways and often results from cumulative impacts over time. Assessment requires monitoring various ecological indicators.

        ### Key Indicators
        - Vegetation Structure and Composition
        - Species Diversity and Abundance
        - Soil Quality and Erosion
        - Water Resource Condition

        ### Major Causes
        Primary factors contributing to habitat degradation:

        - Overgrazing and Resource Extraction
        - Pollution and Contamination
        - Invasive Species
        - Climate Change Impacts

        ### Management Responses
        Essential elements of degradation management:

        - Regular Monitoring Programs
        - Restoration Initiatives
        - Pressure Reduction
        - Adaptive Management
        """)

    # Tab 5: Climate Change
    with tabs[4]:
        st.header("Climate Change Impacts")
        
        st.markdown("""
        ### Climate Change Context
        Protected areas face unprecedented challenges from climate change, requiring adaptation of management strategies and conservation approaches.

        ### Primary Impacts
        - Temperature and Precipitation Changes
        - Extreme Weather Events
        - Species Range Shifts
        - Ecosystem Process Disruption

        ### Vulnerability Assessment
        Key factors in assessing climate vulnerability:

        - Exposure to Climate Changes
        - Ecosystem Sensitivity
        - Adaptive Capacity
        - Current Stressors

        ### Adaptation Strategies
        Protected areas must develop comprehensive adaptation approaches:

        - Corridor Enhancement
        - Species Translocation Programs
        - Habitat Restoration
        - Water Management Systems
        """)

    # Tab 6: Funding
    with tabs[5]:
        st.header("Protected Area Funding")
        
        st.markdown("""
        ### Funding Fundamentals
        Sustainable funding remains critical for effective protected area management. Understanding diverse funding sources and mechanisms is essential.

        ### Cost Categories
        - Operational Costs (staff, maintenance)
        - Program Implementation
        - Infrastructure Development
        - Research and Monitoring

        ### Funding Sources
        Protected areas typically rely on multiple funding streams:

        - Government Allocations
        - Tourism Revenue
        - International Donors
        - Innovative Mechanisms

        ### Financial Sustainability
        Key elements for long-term financial stability:

        - Revenue Diversification
        - Endowment Development
        - Community Enterprises
        - Payment for Ecosystem Services
        """)
