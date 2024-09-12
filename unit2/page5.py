import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Default values for populations and time steps
default_values = {
    'algae_population': 300,
    'mollusk_population': 150,
    'sculpin_population': 50,
    'salmon_population': 5,
    'time_steps': 50
}

# Function to reset all values to their defaults
def reset_defaults():
    for key, value in default_values.items():
        st.session_state[key] = value

# Initialize session state for slider values
for key, value in default_values.items():
    if key not in st.session_state:
        st.session_state[key] = value

def page5_content():
    # Page Title
    st.title("Ecosystem Diversity: Lake Food Chain Simulation with Predator Satiation")

    # Introduction to Ecosystem Diversity
    st.write("""
    **Ecosystem diversity** includes the variety of ecosystems and the interactions between organisms and their environments. 
    This simulation explores food chains (trophic dynamics) in a lake ecosystem.
    """)
    
    # HTML and CSS for dynamic resizing and centering
    html_code = """
    <div style="display: flex; justify-content: center; width: 100%; margin-bottom: 20px;">
        <div style="width: 50%;">
            <img src="https://openstax.org/apps/archive/20240812.170248/resources/d2b636a215efb1ec7f1a55221e684d1410da22e3" style="width: 100%;">
        </div>
    </div>
    """
    
    # Render the HTML
    st.markdown(html_code, unsafe_allow_html=True)
    st.markdown("Figure from [Openstax](https://openstax.org/details/books/biology-2e)")
    st.subheader("Lake Food Chain")
    st.write("""
    A typical grassland food chain might include:
    - **Producers**: Algae
    - **Primary Consumers**: Mollusks
    - **Secondary Consumers**: Slimy sculpin
    - **Tertiary Consumers**: Chinook salmon
    """)

    # Button to reset sliders to default values
    if st.button("Click for Initial Community"):
        reset_defaults()

    # Interactive Simulation Controls
    st.subheader("Adjust Initial Population Sizes")

    # Sliders for initial population sizes using session state, without default values set directly in sliders
    st.slider(
        "Initial Number of algae (Producers)", 
        min_value=0, max_value=500, 
        step=10, 
        key='algae_population'
    )
    st.slider(
        "Initial Number of mollusks (Primary Consumers)", 
        min_value=0, max_value=500, 
        step=10, 
        key='mollusk_population'
    )
    st.slider(
        "Initial Number of slimy sculpins (Secondary Consumers)", 
        min_value=0, max_value=200, 
        step=5, 
        key='sculpin_population'
    )
    st.slider(
        "Initial Number of chinook salmon (Tertiary Consumers)", 
        min_value=0, max_value=50, 
        step=1, 
        key='salmon_population'
    )
    st.slider(
        "Number of Time Steps", 
        min_value=10, max_value=500, 
        step=10, 
        key='time_steps'
    )

    # Parameters for the Lotka-Volterra model with predator satiation
    K = 300  # Carrying capacity for algae
    algae_growth_rate = 0.2  # Growth rate for algae
    mollusk_consumption_rate = 0.005  # Reduced consumption rate of grass by mollusk
    mollusk_growth_rate = 0.15  # Reduced growth rate for mollusk, more dependent on grass availability
    mouse_attack_rate = 0.007  # Attack rate of sculpin on mollusk
    mouse_handling_time = 0.05  # Handling time of mollusk by sculpin
    mouse_growth_rate = 0.1  # Reproduction rate of sculpin per grasshopper eaten
    mouse_mortality_rate = 0.03  # Natural mortality rate of sculpin
    salmon_attack_rate = 0.008  # Attack rate of salmon on sculpin
    salmon_handling_time = 0.05  # Handling time of sculpin by salmon
    salmon_growth_rate = 0.08  # Reproduction rate of salmon per mouse eaten
    salmon_mortality_rate = 0.04  # Natural mortality rate of salmon

    # Simulation Button
    if st.button("Simulate"):
        # Initialize lists to store population sizes over time
        algae_populations = [st.session_state.algae_population]
        mollusk_populations = [st.session_state.mollusk_population]
        sculpin_populations = [st.session_state.sculpin_population]
        salmon_populations = [st.session_state.salmon_population]

        # Time-based simulation using satiation parameters
        for t in range(st.session_state.time_steps):
            # Previous populations
            G = algae_populations[-1]  # Grass population
            N = mollusk_populations[-1]  # Grasshopper population
            P = sculpin_populations[-1]  # Mouse population
            H = salmon_populations[-1]  # Hawk population

            # Grass dynamics with logistic growth and reduced consumption by mollusk
            new_algae_population = max(G + algae_growth_rate * G * (1 - G / K) - mollusk_consumption_rate * N * G, 0)
            
            # Grasshopper dynamics influenced by reduced grass consumption rate and predation by sculpin
            mollusk_consumed_by_sculpin = (mouse_attack_rate * N * P) / (1 + mouse_attack_rate * mouse_handling_time * N)
            new_mollusk_population = max(N + mollusk_growth_rate * N * (G / (G + 1)) - mollusk_consumed_by_sculpin, 0)
            
            # sculpin dynamics influenced by grasshopper availability and predation by salmon with satiation
            sculpin_consumed_by_salmon = (salmon_attack_rate * P * H) / (1 + salmon_attack_rate * salmon_handling_time * P)
            new_sculpin_population = max(P + mouse_growth_rate * mollusk_consumed_by_sculpin - mouse_mortality_rate * P - sculpin_consumed_by_salmon, 0)
            
            # salmon dynamics influenced by mouse availability with satiation
            new_salmon_population = max(H + salmon_growth_rate * sculpin_consumed_by_salmon - salmon_mortality_rate * H, 0)

            # Append new populations to lists
            algae_populations.append(new_algae_population)
            mollusk_populations.append(new_mollusk_population)
            sculpin_populations.append(new_sculpin_population)
            salmon_populations.append(new_salmon_population)

        # Create the time array with the same length as the population lists
        time = np.arange(0, st.session_state.time_steps + 1)

        # Plotting
        fig, ax = plt.subplots(figsize=(8, 5))

        ax.plot(time, algae_populations, label='Algae (Producers)', color='green')
        ax.plot(time, mollusk_populations, label='Mollusk (Primary Consumers)', color='orange')
        ax.plot(time, sculpin_populations, label='Sculpins (Secondary Consumers)', color='red')
        ax.plot(time, salmon_populations, label='Salmon (Tertiary Consumers)', color='blue')

        ax.set_xlabel('Time Steps')
        ax.set_ylabel('Number of Individuals')
        ax.set_title('Population Changes Over Time in Grassland Food Chain')
        ax.legend()

        st.pyplot(fig)

    # Conclusion
    st.write("Question: What happens to populations over time at the different trophic levels if you change the initial population size but leave the rest as they are?")
    
    
    
