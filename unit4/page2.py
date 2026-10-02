import streamlit as st

def page2_content():
    
    st.header("Threats to species")
    
    st.subheader("Threats to different groups of vertebrates")
    
    col1, col2 = st.columns([1, 1])  # The first column is twice as wide as the second

    with col1:
        st.image("./unit4/images/major_threats.png")
        st.markdown("Source: [WWF Living Planet Report (2018)](https://www.worldwildlife.org/pages/living-planet-report-2018)")

    st.write("""
             **Question**: Do all vertebrate groups have the same level of threats? 
             What are the patterns you see? How could they be explained?
             """)
    
    st.subheader("The human footprint (revisited)")
    
    col1, col2 = st.columns([2, 1])  # The first column is twice as wide as the second

    with col1:
        st.image("./unit4/images/degradation.png")
        st.markdown("Source: [WWF Living Planet Report (2018)](https://www.worldwildlife.org/pages/living-planet-report-2018)")

    st.write("""
             **Question**: What are the patterns in habitat degradation over time? Are some
             of these cells related to each other? Are all of them related? Explain.
             """)
    
    st.subheader("The fate of species")
    
    col1, col2 = st.columns([2, 1])  # The first column is twice as wide as the second

    with col1:
        st.image("./unit4/images/red_list_trends.png")
        st.markdown("Source: [WWF Living Planet Report (2018)](https://www.worldwildlife.org/pages/living-planet-report-2018)")

    st.write("""
             The International Union for Conservation of Nature and Natural Resources (IUCN),
             among other things, keeps a list of threatened species (Red List), including
             information about their population trends, biggest threats, and conservation
             efforts. In general, major taxonomic groups are showing a trend towards
             decline.  
             
             We will consider the IUCN Red List in more detail later on in the semester.
             """)
    
    