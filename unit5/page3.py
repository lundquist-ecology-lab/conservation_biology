import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def page3_content():
    # Conservation Equations
    st.header("Species-Area Curve")

    # Display the Species-Area Relationship equation
    st.markdown(r"""
    ### Species-Area Relationship (SAR) Equation:
    $$
    S = c \cdot A^z
    $$
    Where:
    - S is the number of species,
    - A is the area of habitat,
    - c is a constant,
    - z is the slope of the curve (affecting how species richness scales with area).
    """)

    # Slider to adjust area (in relation to the largest possible area)
    area = st.slider("Area of Habitat Conserved (in square km)", 0.1, 1000.0, 100.0)

    # Constants for the SAR equation
    c = 10  # Base constant for the number of species at a unit area
    z = st.slider("SAR Exponent (z)", 0.1, 0.5, 0.3)  # User can adjust the exponent

    # Calculate species richness based on area
    species_richness_sar = c * (area ** z)

    # Display calculated species richness
    st.write(f"Estimated Species Richness: {species_richness_sar:.2f}")

    # Plot the species-area curve
    area_range = np.linspace(0.1, 1000, 500)  # Range of area sizes
    species_range = c * (area_range ** z)  # Corresponding species richness

    fig, ax = plt.subplots()
    ax.plot(area_range, species_range, label=f'SAR curve (c={c}, z={z})', color='green')

    ax.set_xlabel('Area (square km)')
    ax.set_ylabel('Species Richness')
    ax.set_title('Species-Area Curve')
    ax.legend()

    st.pyplot(fig)

    # Discussion Questions
    st.header("Discussion Questions")
    st.markdown("""
    1. How does increasing the area of the habitat affect species richness based on the SAR equation? Why might this be important for conservation planning?
    3. In what ways could habitat fragmentation impact the number of species in a given region?
    4. How could the SAR help us prioritize areas for conservation?
    """)
