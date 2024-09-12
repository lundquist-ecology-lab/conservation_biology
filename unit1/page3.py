import streamlit as st

def page3_content():
    st.header("Major global issues in Conservation Biology")
    st.write("Ecological footprints")
    st.image("https://worldmapper.org/wp-content/uploads/2019/07/Grid_EcologicalFootprint_2019.png", use_column_width=True, caption="Ecological Footprint Map 2019")
    st.write("From WorldMapper.org: This map shows the land surface resized by its total ecological footprint in each area interpolated from a population grid and national-level data for each country’s ecological footprint. Each transformed grid cell in the map is proportional to the total number of people living in that area multiplied by their respective national ecological footprint measured in global hectares consumption per capita.")

