import streamlit as st

def page1_content():
    st.title("Biome group activity")
    
    st.header("What is going on with our biomes?")
    
    st.write("""
             **Assignment**: in a group of two or three choose a 
             terrestrial or aquatic biome and answer the following questions.
             """)
    
    st.write("1) What are the primary climatic/aquatic properties of your biome?")
    
    st.write("""
             2) What sort of plants/organisms 
             would you expect to find there?
             """)
    
    st.write("""
             3) Based on your textbook and internet searches, describe 
             up to five anthropogenic threats to those biomes.
             """)
    
    st.write("Write all answers on piece of paper with the names of all members on it.")
    
    
    st.subheader("Example: The Mississippi River Delta")
    
    st.write("""
             The Mississippi River Delta is an estuary, which is an aquatic biome.
             It is characterized by being a mixture of freshwater (Mississippi River),
             and salt water (Gulf of Mexico). 
             """)
    
    st.write("""
             There is a high level of biodiversity in estuaries due to the high
             level of habitat diversity caused by the mix of salt, fresh, and brackish
             water. You would also expect to find salt marshes (a type of wetland) that
             also support plant and animal life uniquely adapted to tidal cycles
             and variable salinity.
             """)
    
    st.write("""
            Anthropogenic threats:

            1) Increase nutrient runoff (N and P) from  farms in the Great Plains
            2) Reduced habitat space for organisms due to urbanization
            3) Decreased resilience to tropical storms due to loss of coastal habitat and increase urbanization
            4) Ground water salinization due to overuse of freshwater aquifers
            5) Oil spills (e.g., Deepwater Horizon) have had immediate and long-term effects on biota and water quality
            """)
    
    
    # Load your images
    image1 = './unit4/images/deadzone.webp'
    image2 = './unit4/images/katrina.webp'
    image3 = './unit4/images/oil.webp'

    # Create three columns
    col1, col2, col3 = st.columns(3)

    # Display images in each column
    with col1:
        st.image(image1, caption="Credit: Carleton College", use_column_width=True)

    with col2:
        st.image(image2, caption="Credit: The History Channel", use_column_width=True)

    with col3:
        st.image(image3, caption="Credit: The New Yorker", use_column_width=True)