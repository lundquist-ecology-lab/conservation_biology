import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def page5_content():
    # Title and description
    st.title('Climate Change and Emergence Times')
    st.write('Adjust the temperature regime and select which species reacts to see how it affects the emergence times in a temperate biome.')

    # Temperature change slider
    temp_change = st.slider('Temperature Change (°C)', -5, 5, 0)

    # Allow the user to choose which species reacts to the climate change
    reacting_species = st.selectbox('Select the species that reacts to the temperature change:',
                                    ['Flowers', 'Bees', 'Dragonflies', 'None'])

    # Baseline emergence times (days from start of year)
    flowers_baseline = 100  # Example day
    bees_baseline = 120
    dragonflies_baseline = 140

    # Adjust the emergence time of the reacting species based on the temperature
    def adjust_emergence(baseline, temp_change, reacting_species, species_name):
        if reacting_species == species_name:
            return baseline - (temp_change * 3)  # Assume 3 days change per °C
        return baseline  # No change for non-reacting species

    # Adjust each species based on the selected reaction
    flowers_emergence = adjust_emergence(flowers_baseline, temp_change, reacting_species, 'Flowers')
    bees_emergence = adjust_emergence(bees_baseline, temp_change, reacting_species, 'Bees')
    dragonflies_emergence = adjust_emergence(dragonflies_baseline, temp_change, reacting_species, 'Dragonflies')

    # Plotting single peak and valley for each species using a Gaussian-like curve
    days = np.arange(50, 200)
    fig, ax = plt.subplots()

    ax.plot(days, np.exp(-0.01 * (days - flowers_emergence)**2), label='Flowers', color='green')
    ax.plot(days, np.exp(-0.002 * (days - bees_emergence)**2), label='Bees', color='orange')
    ax.plot(days, np.exp(-0.001 * (days - dragonflies_emergence)**2), label='Dragonflies', color='blue')

    # Customize plot appearance
    ax.set_xlabel('Day of the Year')
    ax.set_ylabel('Emergence/Flowering Intensity')
    ax.legend()

    # Display the plot
    st.pyplot(fig)

    # Display the new emergence times
    st.write(f'Flowering Time: Day {flowers_emergence:.1f}')
    st.write(f'Bee Emergence Time: Day {bees_emergence:.1f}')
    st.write(f'Dragonfly Emergence Time: Day {dragonflies_emergence:.1f}')
    
    
    # Discussion questions section
    st.header("Discussion Questions")

    st.markdown("**1. Phenological Mismatch**")
    st.write("Based on your observations from adjusting the temperature in the simulation, how might changes in the emergence times of flowers, bees, and dragonflies affect their interactions? What are the potential consequences if one species emerges earlier or later than another?")

    st.markdown("**2. Climate Change and Ecosystem Services**")
    st.write("Bees are critical for pollination, which is essential for the survival of many plants, including crops. How could changes in bee emergence times due to climate change impact pollination, and what effects might this have on both natural ecosystems and human agriculture?")

    st.markdown("**3. Species Adaptation**")
    st.write("Do you think all species (flowers, bees, dragonflies) are equally able to adapt to changes in temperature? What factors might influence a species’ ability to shift its emergence time in response to climate change?")

    st.markdown("**4. Broader Ecological Impacts**")
    st.write("In this simulation, we focused on temperature and emergence times of three species. How might other climate-related factors (such as changes in precipitation or habitat availability) interact with these temperature changes to affect ecosystems? How might these factors influence biodiversity in a temperate biome?")

