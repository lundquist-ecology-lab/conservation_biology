import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO

def page4_content():
    # Page Title
    st.title("Understanding Genetic Diversity in Wild Populations")

    # Introduction
    st.write("""
    **Genetic diversity** refers to the total number of genetic characteristics in the genetic makeup of a species. It is a fundamental component of biodiversity and plays a critical role in the adaptability and survival of species. Higher genetic diversity within a population means that the species has a greater chance of surviving environmental changes, diseases, and other threats.
    """)

    # Importance of Genetic Diversity
    st.subheader("Why is Genetic Diversity Important?")
    st.write("""
    1. **Adaptability to Environmental Changes**: Populations with high genetic diversity have a wider range of traits, which increases the likelihood that some individuals will survive in changing environments.
    2. **Resistance to Diseases and Pests**: Greater genetic variation allows populations to better resist diseases and pests, ensuring their long-term survival.
    3. **Prevention of Inbreeding Depression**: Inbreeding, or breeding between closely related individuals, reduces genetic diversity and can result in inbreeding depression, where harmful genetic traits become more common.
    4. **Conservation Value**: Conserving genetic diversity is essential for maintaining ecosystem services and resilience. It is a key focus in wildlife conservation efforts.
    """)

    # Simulation of Genetic Diversity
    st.subheader("Simulation: Visualizing Genetic Diversity")

    # Slider for population size
    population_size = st.slider("Select Population Size", min_value=10, max_value=200, value=50, step=10)

    # Number of different alleles
    num_alleles = st.slider("Select Number of Different Alleles", min_value=2, max_value=10, value=4)

    # Generate random genetic data for simulation
    genetic_data = np.random.randint(0, num_alleles, population_size)

    # Plot simulation
    fig, ax = plt.subplots()

    # Create scatter plot of genetic data
    colors = plt.cm.tab10(genetic_data / max(genetic_data))
    ax.scatter(np.arange(population_size), np.zeros(population_size), c=colors, s=100)

    ax.set_yticks([])
    ax.set_xticks([])
    ax.set_title("Genetic Diversity Simulation: Each Circle Represents an Individual")

    # Save the plot to a buffer
    buf = BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode()

    # Display plot with custom HTML for 50% width
    html_code = f"""
    <div style="display: flex; justify-content: center; width: 100%; margin-bottom: 20px;">
        <div style="width: 75%;">
            <img src="data:image/png;base64,{image_base64}" style="width: 100%;">
        </div>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)

    # Explanation of Simulation
    st.write("""
    In this simulation:
    - Each circle represents an individual in the population.
    - The color of each circle represents a different genetic trait or allele.
    - Adjust the sliders to see how genetic diversity changes with population size and the number of alleles.
    
    **Allele**: the sequence of DNA (ATCG) at a particular gene. Genes can have many different
    alleles. The more the alleles, the more genetic diversity at that particular gene.
    """)
    
    st.write("""
               **Question**: If you set alleles to 2 and shift between 10 and 20 individuals, what
               happens to the relative abundance of each allele? Why might this be an
               issue in small populations?
                """)

    # Measures of Genetic Diversity
    st.subheader("How is Genetic Diversity Measured?")
    st.write("""
    There are several ways to measure genetic diversity in wild populations:
    - **Allelic Richness**: The total number of different alleles present in a population.
    - **Heterozygosity**: The proportion of individuals in a population that have two different alleles at a particular gene locus.
    - **Genetic Distance**: A measure of the genetic difference between populations, often used to study the evolutionary relationships between species.
    - **Genomic Methods**: Modern genomic techniques such as SNP (Single Nucleotide Polymorphism) analysis and whole-genome sequencing allow for comprehensive assessments of genetic diversity at a very fine scale.
    """)

    # Example: Genetic Diversity in Wild Populations
    st.subheader("Genetic Diversity in Wild Populations")
    st.write("""
    Let's consider an example of genetic diversity in a wild population:

    **Cheetahs (*Acinonyx jubatus*) have low genetic diversity due to natural events**
    - Cheetahs have markedly low genetic diversity, leading to issues of inbreeding depression in captivity. This low genetic diversity was likely caused by a **bottleneck** event some 100,000 years ago and again around 12,000 years ago. Their genetic diversity is lower than that of domesticated animals.
    """)
    
    # HTML and CSS for dynamic resizing and centering
    html_code = """
    <div style="display: flex; justify-content: center; width: 100%; margin-bottom: 20px;">
        <div style="width: 50%;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Male_cheetah_facing_left_in_South_Africa.jpg/1920px-Male_cheetah_facing_left_in_South_Africa.jpg" style="width: 100%;">
        </div>
    </div>
    """
    
    # Render the HTML
    st.markdown(html_code, unsafe_allow_html=True)
    
    
    st.write("""
    **The Florida Panther (*Puma concolor coryi*) have low genetic diversity due to human actions**:
    - The Florida panther is a subspecies of the cougar that faced severe inbreeding depression due to a small population size and habitat loss. Conservationists introduced Texas cougars to increase genetic diversity, which helped reduce health problems and improve population viability.
    """)
    
    # HTML and CSS for dynamic resizing and centering
    html_code = """
    <div style="display: flex; justify-content: center; width: 100%; margin-bottom: 20px;">
        <div style="width: 50%;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/3/37/Everglades_National_Park_Florida_Panther.jpg" style="width: 100%;">
        </div>
    </div>
    """
    
    # Render the HTML
    st.markdown(html_code, unsafe_allow_html=True)
