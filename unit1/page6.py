import streamlit as st

def page6_content():
    st.header("Key Figures in Conservation Biology")
    
    st.subheader("Religious and Cultural Beliefs")
    st.write("Native Americans, Hinduism, Jainism, Taoism, Buddhism, Islam, Judaic, Christianity, etc.")
    st.image(
        "https://images.nationalgeographic.org/image/upload/t_edhub_resource_key_image/v1638892509/EducationHub/photos/mahavira.jpg", 
        caption="Mahavira, the Jain teacher of dharma (National Geographic)", 
        use_column_width=True
    )
    st.subheader("Authors")
    st.write("Ralph Waldo Emerson, Henry David Thoreau, Aldo Leopold, Rachel Carson")
    
    # Create two columns for the first two images
    col1, col2 = st.columns(2)

    with col1:
        st.image("https://blog.response.restoration.noaa.gov/sites/default/files/inline-images/unnamed%20%2813%29.png", caption="Rachel Carson (USFWS)", use_column_width=True)
    
    with col2:
        st.image("https://upload.wikimedia.org/wikipedia/en/a/ac/SilentSpring.jpg", caption="Silent Spring", use_column_width=True)

    st.subheader("Photographers")
    st.write("Ansel Adams, Brian Skerry")
    col3, col4 = st.columns(2)
    
    with col3:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Ansel_Adams_and_camera.jpg/800px-Ansel_Adams_and_camera.jpg", caption="Ansel Adams", use_column_width=True)
    
    with col4:
    # Create a single column for the wide image
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Looking_across_lake_toward_mountains%2C_%22Evening%2C_McDonald_Lake%2C_Glacier_National_Park%2C%22_Montana.%2C_1933_-_1942_-_NARA_-_519861.jpg/1024px-Looking_across_lake_toward_mountains%2C_%22Evening%2C_McDonald_Lake%2C_Glacier_National_Park%2C%22_Montana.%2C_1933_-_1942_-_NARA_-_519861.jpg", caption="Landscape by Ansel Adams", use_column_width=True)

    col5, col6 = st.columns(2)
    
    with col5:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Brian_Skerry.JPG/1024px-Brian_Skerry.JPG", caption="Brian Skerry", use_column_width=True)
    
    with col6:
    # Create a single column for the wide image
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Killerwhales_jumping.jpg/1280px-Killerwhales_jumping.jpg", caption="Secrets of Whales", use_column_width=True)

    st.subheader("Public Figures")
    st.write("John Muir, Gifford Pinchot")
    
    col7, col8 = st.columns(2)
    
    with col7:
        st.image("https://upload.wikimedia.org/wikipedia/commons/9/98/John_Muir_by_Carleton_Watkins%2C_c1875.jpg", caption="John Muir", use_column_width=True)
    
    with col8:
    # Create a single column for the wide image
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Gifford_Pinchot_3c03915u.jpg/800px-Gifford_Pinchot_3c03915u.jpg", caption="Gifford Pinchot", use_column_width=True)