import streamlit as st
import pandas as pd
from collections import Counter
from math import log
import requests
from PIL import Image
from io import BytesIO

def page3_content():
    # Load the data
    url = "https://raw.githubusercontent.com/lundquist-ecology-lab/urban_aquatic_insects/main/data/stream_insects.csv"
    data = pd.read_csv(url)

    # Filter data for the year 2014 and family level
    data_2014 = data[data['year'] == 2014]

    # Function to calculate alpha diversity (species richness)
    def alpha_diversity_richness(df, group_column):
        grouped = df.groupby(group_column)
        richness_scores = {name: group['family'].nunique() for name, group in grouped}
        return richness_scores

    # Function to calculate Shannon diversity
    def shannon_diversity(df, group_column):
        grouped = df.groupby(group_column)
        diversity_scores = {}

        for name, group in grouped:
            counts = Counter(group['family'])
            total = sum(counts.values())
            diversity = -sum((count / total) * log(count / total) for count in counts.values() if count > 0)
            diversity_scores[name] = diversity

        return diversity_scores

    # Function to calculate gamma diversity
    def gamma_diversity(df):
        counts = Counter(df['family'])
        return len(counts)

    # Function to calculate beta diversity
    def beta_diversity(alpha, gamma):
        alpha_mean = sum(alpha.values()) / len(alpha)
        return gamma / alpha_mean

    # Function to find the most common family
    def most_common_family(df):
        family_counts = Counter(df['family'])
        most_common = family_counts.most_common(1)
        return most_common[0] if most_common else ("None", 0)

    # Function to display an image from a URL
    def display_image_from_url(url, caption):
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        st.image(image, caption=caption, use_column_width=True)

    # User Interface
    st.title("Diversity Analysis for Urban Aquatic Insects in Binghamton, NY")
    

    # Display definitions and formulas
    st.subheader("Definitions")
    st.write("**Alpha Diversity**: The number of different families (species richness) within a particular site or habitat.")
    st.write("**Gamma Diversity**: The total number of different families across all sites or habitats.")
    st.write("**Beta Diversity**: The ratio of gamma diversity to the average alpha diversity, indicating the turnover of species between sites.")
    st.latex(r"\beta = \frac{\gamma}{\bar{\alpha}}")

    st.write("**Shannon Diversity Index**")
    st.latex(r"H = -\sum_{i=1}^S p_i \ln(p_i)")
    st.write("where:")
    st.latex(r"H = \text{Shannon diversity index}")
    st.latex(r"S = \text{Number of species (families in this case)}")
    st.latex(r"p_i = \text{Proportion of individuals of species } i")


    # Data Background
    st.write("**Background**")
    
    st.write("""
             In 2014, a scientist went out to five streams in Bingahmton, NY, a
             medium-sized city in upstate New York. Each of these streams were unique
             because they flowed through rural landscape in their upstream portion,
             and flowed through urban landscape in their downstream portion where 
             they drained into the Susquehanna River. 
             
             The scientist was interested to see if there was an impact on urbanization
             on the aquatic insect biodiversity in the downstream portions of these
             rivers versus their upstream portions. The upstream portions were of each stream were considered 'rural' 
             and the downstream portions were considered 'urban'. 
             
             Below is the analysis of alpha, gamma, and beta diversity for urban and rural
             sites as well as Shannon Diversity. Using these results, describe the patterns of biodiversity in these
             streams.
             
             """)
    
    st.write("**Map of Binghamton sites (red = urban landscape)**")
    # HTML and CSS for dynamic resizing and centering
    html_code = """
    <div style="display: flex; justify-content: center; width: 100%; margin-bottom: 20px;">
        <div style="width: 75%;">
            <img src="https://github.com/lundquist-ecology-lab/urban_aquatic_insects/blob/main/figures/map.jpg?raw=true" style="width: 100%;">
        </div>
    </div>
    """
    
    # Render the HTML
    st.markdown(html_code, unsafe_allow_html=True)
    
    # Display data preview
    st.write("### Dataset Preview")
    st.dataframe(data_2014.head())

    # Select site type for analysis
    site_type = st.selectbox("Select Site Type", ['urban', 'rural', 'both'])

    # Filter data based on the selected site type
    if site_type in ['urban', 'rural']:
        filtered_data = data_2014[data_2014['type'] == site_type]
    else:
        filtered_data = data_2014

    # Calculate alpha diversity
    st.write(f"**Alpha Diversity (Richness) for {site_type.capitalize()} Sites**")
    alpha_scores = alpha_diversity_richness(filtered_data, 'site')
    st.write(alpha_scores)

    # Calculate gamma diversity
    st.write("**Gamma Diversity**")
    gamma_score = gamma_diversity(filtered_data)
    st.write(f"Gamma Diversity: {gamma_score}")

    # Calculate beta diversity
    st.write("**Beta Diversity**")
    beta_score = beta_diversity(alpha_scores, gamma_score)
    st.write(f"Beta Diversity: {beta_score}")

    # Calculate Shannon diversity
    st.write("**Shannon Diversity for Each Site Type**")
    shannon_scores = shannon_diversity(filtered_data, 'site')
    st.write(shannon_scores)

    # Determine the most common family for the selected site type
    most_common = most_common_family(filtered_data)
    st.write(f"**Most Common Family in {site_type.capitalize()} Sites: {most_common[0]} ({most_common[1]} individuals)**")

    # Display image of the most common family
    # Replace this URL with an actual URL of an image representing the most common family
    image_urls = {
        'urban': "https://static.macroinvertebrates.org/gigapans/191254/images.25e2731ca9b6e7904857b2faa229966b/191254-800x544.jpg",  # Replace with a real image URL
        'rural': "https://static.macroinvertebrates.org/gigapans/191254/images.25e2731ca9b6e7904857b2faa229966b/191254-800x544.jpg",  # Replace with a real image URL
        'both': "https://static.macroinvertebrates.org/gigapans/191254/images.25e2731ca9b6e7904857b2faa229966b/191254-800x544.jpg"     # Replace with a real image URL
    }

    if most_common[0] != "None":
        # st.write(f"#### Image of {most_common[0]} ({site_type.capitalize()} Sites)")
        display_image_from_url(image_urls[site_type], f"Image of {most_common[0]}")
