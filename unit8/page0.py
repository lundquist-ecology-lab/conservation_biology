import streamlit as st

def page0_content():
    st.title("Protected Areas: Terrestrial and Marine Conservation")
    st.markdown("---")

    tabs = st.tabs([
        "IUCN Categories", 
        "Protected Area Types", 
        "Marine Challenges",
        "Degazettement",
        "Gap Analysis",
        "Design & Biogeography",
        "Networks & Corridors"
    ])

    # Tab 1: IUCN Categories
    with tabs[0]:
        st.header("IUCN Protected Area Categories")
        
        st.markdown("""
        ### Overview
        The IUCN Protected Area Categories represent a global system for classifying protected areas based on their management objectives and levels of protection.

        ### Category Ia: Strict Nature Reserve
        These areas represent the highest level of protection:
        - Strictly controlled access
        - Focus on biodiversity and geological preservation
        - Scientific research under strict guidelines
        
        ### Category Ib: Wilderness Area
        Large natural areas with minimal human influence:
        - Preservation of natural conditions
        - Limited public access
        - Basic recreational activities permitted
        
        ### Category II: National Park
        Extensive natural areas balancing protection with public use:
        - Protection of ecological processes
        - Recreational and educational opportunities
        - Visitor facilities and infrastructure
        
        ### Category III: Natural Monument
        Protection of specific natural features:
        - Focus on unique geological or biological features
        - Often smaller in size
        - Higher visitor access permitted
        
        ### Category IV: Habitat Management Area
        Active management for species or habitat conservation:
        - Regular intervention allowed
        - Species-specific management
        - Habitat maintenance programs
        """)

    # Tab 2: Protected Area Types
    with tabs[1]:
        st.header("Terrestrial vs Marine Protected Areas")
        
        st.markdown("""
        ### Introduction
        Protected areas vary significantly between terrestrial and marine environments, each presenting unique management challenges and opportunities.

        ### Terrestrial Protected Areas
        Characteristics and advantages:
        - Fixed, clearly defined boundaries
        - Established monitoring methods
        - Well-developed management practices
        - Extensive research base

        Management considerations:
        - Infrastructure development
        - Access control
        - Habitat maintenance
        - Visitor management
        
        ### Marine Protected Areas
        Unique challenges and features:
        - Three-dimensional boundaries
        - Mobile protection targets
        - Complex ecosystem interactions
        - Monitoring difficulties

        Specialized requirements:
        - Advanced technology needs
        - Weather-dependent operations
        - International cooperation
        - Specialized staff training
        """)

    # Tab 3: Marine Challenges
    with tabs[2]:
        st.header("Issues with Marine Protected Areas")
        
        st.markdown("""
        ### Introduction
        Marine protected areas face unique challenges due to their dynamic nature and the complexity of marine ecosystems.

        ### Enforcement Challenges
        Key issues in maintaining protection:
        - Boundary monitoring difficulties
        - International jurisdiction
        - Equipment and training needs
        - Cost-intensive operations

        ### Ecological Considerations
        Understanding marine dynamics:
        - Species movement patterns
        - Ecosystem connectivity
        - Larval dispersal
        - Population monitoring

        ### Management Challenges
        Operational issues:
        - Weather constraints
        - Technical limitations
        - Deep water access
        - Resource allocation
        """)

    # Tab 4: Degazettement
    with tabs[3]:
        st.header("Protected Area Degazettement")
        
        st.markdown("""
        ### Understanding Degazettement
        Degazettement refers to the legal process of removing or reducing protected status from an area, often with significant conservation implications.

        ### Primary Causes
        Economic factors:
        - Development pressure
        - Resource demands
        - Infrastructure needs

        Political factors:
        - Policy shifts
        - Resource reallocation
        - Legal changes

        Management issues:
        - Funding shortfalls
        - Protection effectiveness
        - Staffing problems

        ### Impact Assessment
        Major consequences:
        - Biodiversity loss
        - Ecosystem fragmentation
        - Service reduction
        - Community effects

        ### Prevention Approaches
        Key strategies:
        - Legal protection
        - Sustainable financing
        - Community engagement
        - Regular assessment
        """)

    # Tab 5: Gap Analysis
    with tabs[4]:
        st.header("Protected Area Gap Analysis")
        
        st.markdown("""
        ### Introduction
        Gap analysis evaluates the effectiveness and completeness of protected area networks in conserving biodiversity.

        ### Assessment Components
        Representation analysis:
        - Ecosystem coverage
        - Species protection
        - Habitat types

        Ecological evaluation:
        - Connectivity assessment
        - Core area adequacy
        - Buffer requirements

        Management review:
        - Resource evaluation
        - Capacity assessment
        - Infrastructure review

        ### Implementation Process
        Systematic approach:
        - Target identification
        - Current status assessment
        - Gap identification
        - Action prioritization
        - Solution implementation
        """)

    # Tab 6: Design & Biogeography
    with tabs[5]:
        st.header("Protected Area Design & Island Biogeography")
        
        st.markdown("""
        ### Introduction
        Island biogeography principles guide protected area design by helping understand species-area relationships and isolation effects.

        ### Fundamental Concepts
        Species-area relationships:
        - Area size influence
        - Population viability
        - Habitat requirements

        Isolation effects:
        - Migration patterns
        - Genetic exchange
        - Colonization rates

        ### Design Considerations
        SLOSS debate:
        - Size vs. number trade-offs
        - Edge effect management
        - Species requirements

        Shape optimization:
        - Edge minimization
        - Core area protection
        - Connectivity enhancement
        """)

    # Tab 7: Networks & Corridors
    with tabs[6]:
        st.header("Protected Area Networks and Habitat Corridors")
        
        st.markdown("""
        ### Introduction
        Protected area networks enhance conservation effectiveness through connected systems of protected areas and corridors.

        ### Network Structure
        Core components:
        - Primary conservation zones
        - Critical habitats
        - Breeding areas

        Support zones:
        - Buffer areas
        - Traditional use zones
        - Transition zones

        ### Corridor Systems
        Linear connections:
        - Riparian corridors
        - Wildlife passages
        - Habitat strips

        Landscape integration:
        - Habitat mosaics
        - Multi-use zones
        - Regional linkages

        ### Conservation Benefits
        Network advantages:
        - Genetic diversity
        - Climate resilience
        - Species movement
        - Ecosystem stability
        """)