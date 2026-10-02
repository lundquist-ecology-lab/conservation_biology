import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def page2_content():
    # Title and introduction
    st.title('Island Biogeography and Extinction Rates')
    st.write("""
    Island biogeography theory explains how species richness on islands is influenced by island size, distance from the mainland, 
    immigration, and extinction rates. This page simulates both the theoretical curves and dynamic changes over time.
    """)

    # Display the Island Biogeography equation
    st.markdown(r"""
    ### Island Biogeography Equation:
    $$
    S_{eq} = \frac{I \cdot E}{I + E}
    $$
    Where:
    - $S_{eq}$ is the equilibrium number of species,
    - $I$ is the immigration rate,
    - $E$ is the extinction rate.
    """)

    st.header("Theoretical Island Biogeography Curves")

    # Plotting the theoretical immigration and extinction curves
    def theoretical_curves():
        species_count = np.linspace(0, 100, 100)

        # Immigration and extinction rates
        large_island_extinction = 0.01 * species_count**1.5
        small_island_extinction = 0.02 * species_count**1.5
        near_island_immigration = 0.3 * np.exp(-0.03 * species_count)
        far_island_immigration = 0.2 * np.exp(-0.03 * species_count)

        fig, ax1 = plt.subplots()

        ax1.set_xlabel('Number of Species')
        ax1.set_ylabel('Immigration Rate', color='blue')
        ax1.plot(species_count, near_island_immigration, label='Near Island (Immigration)', color='blue', linestyle='--')
        ax1.plot(species_count, far_island_immigration, label='Far Island (Immigration)', color='blue')
        ax1.tick_params(axis='y', labelcolor='blue')

        ax2 = ax1.twinx()
        ax2.set_ylabel('Extinction Rate', color='red')
        ax2.plot(species_count, large_island_extinction, label='Large Island (Extinction)', color='red', linestyle='--')
        ax2.plot(species_count, small_island_extinction, label='Small Island (Extinction)', color='red')
        ax2.tick_params(axis='y', labelcolor='red')

        fig.tight_layout()
        st.pyplot(fig)

    theoretical_curves()

    st.write("""
    - Near island/Large island = dotted line  
    - Far island/Small island = solid line    
    """) 

    # Discussion Questions
    st.header("Discussion Questions")

    st.markdown("**1. Island Size and Extinction**")
    st.write("How does island size influence the extinction rate of species? What patterns do you observe when smaller islands are compared to larger ones?")

    st.markdown("**2. Distance from Mainland and Immigration**")
    st.write("What effect does the distance from the mainland have on the immigration rate of species? How do these changes affect the overall species richness on the island?")

    st.markdown("**3. Equilibrium of Species**")
    st.write("Island biogeography theory suggests that an equilibrium is reached where the immigration rate equals the extinction rate. Can you identify this equilibrium in the simulation? How does it change based on island size or distance?")

    st.markdown("**4. Conservation Implications**")
    st.write("How could the concepts from island biogeography inform conservation efforts for isolated habitats such as nature reserves or fragmented ecosystems?")

