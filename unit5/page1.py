import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def page1_content():
    # Introduction to Species Vulnerability to Extinction
    st.header("Factors That Make Species Vulnerable to Extinction")

    st.markdown("""
    Certain species possess traits or face environmental pressures that make them more vulnerable to extinction than others. Understanding these factors can help prioritize conservation efforts and reduce extinction risks.

    Below are some common factors that increase species vulnerability:
    """)

    # Updated list of factors that increase vulnerability
    st.subheader("Factors That Increase Vulnerability:")
    st.markdown("""
    - **Small population size**: Species with small populations are at greater risk of extinction due to inbreeding, genetic bottlenecks, and vulnerability to random environmental changes.
    - **Specialized habitat requirements**: Species dependent on specific habitats are at higher risk if those habitats are degraded or destroyed.
    - **Limited geographic range**: Species that are restricted to small areas are more vulnerable to local changes or habitat destruction.
    - **Low reproductive rate**: Species with low reproductive rates have difficulty recovering from population declines.
    - **Large size**: Larger species often have slower reproductive rates and require more resources, making them more vulnerable to environmental changes.
    - **Permanent or temporary aggregations**: Species that gather in large groups for mating, feeding, or migration may be vulnerable to mass mortality events.
    - **No prior contact with people**: Species that have not evolved alongside humans may lack the necessary behaviors or adaptations to avoid human-induced threats.
    - **Low tolerance to disturbance**: Species sensitive to habitat disturbance (e.g., noise, pollution, human presence) are more likely to suffer in human-modified environments.
    - **Low genetic variability**: Species with little genetic diversity are less adaptable to changing environments and more prone to diseases.
    - **Limited dispersal ability**: Species that cannot easily move between habitats are at higher risk if their habitat is fragmented or destroyed.
    - **Seasonal migration**: Migratory species rely on multiple habitats across seasons, increasing their risk if any of those habitats are altered or destroyed.
    - **Large home range**: Species that require large areas to find food or mates are more vulnerable to habitat loss and fragmentation.
    - **Human exploitation**: Overhunting, overfishing, and trade in wildlife can drive species towards extinction.
    - **Climate change sensitivity**: Species highly sensitive to temperature, rainfall, or seasonal changes are at risk as climate conditions shift.
    """)

    # The Allee Effect Definition and Representation
    st.subheader("The Allee Effect (Aggregations)")

    st.markdown("""
    The **Allee Effect** describes a phenomenon where a species' population growth rate decreases as the population size becomes smaller. This can happen because small populations may have difficulty finding mates, protecting themselves, or fulfilling ecological roles, leading to further declines in population.

    In other words, as the population gets smaller, the chances of extinction increase rather than decrease, which contradicts typical population dynamics where smaller populations might experience faster growth rates.
    """)

    # Allee Effect Example: Flowers in a Field
    st.subheader("Illustration of the Allee Effect: Flowers in a Field")

    st.markdown("""
    Imagine a species of flower in a field. At high population densities, the flowers can easily found by pollinators. However, as the population size decreases, the chances of successful pollination drop, and the flowers may not be able to reproduce effectively. Eventually, this can lead to population collapse.
    
    The graph below represents this effect, showing how a decline in the number of flowers leads to a significant drop in the reproduction rate as the population size falls below a certain threshold.
    """)

    # Simulating Allee Effect for Flowers in a Field
    population_sizes = np.linspace(1, 500, 500)  # Population sizes (flowers)
    reproduction_rate = 0.02 * (population_sizes - 50) * (1 - population_sizes / 500)  # Hypothetical reproduction rate

    fig, ax = plt.subplots()
    ax.plot(population_sizes, reproduction_rate, label="Reproduction Rate (Flowers)", color='green')

    ax.axhline(0, color='black',linewidth=0.5)
    ax.axvline(50, color='red', linestyle='--', label="Allee Threshold")
    ax.set_xlabel('Flower Population Size')
    ax.set_ylabel('Reproduction Rate')
    ax.set_title('The Allee Effect: Flowers in a Field')
    ax.legend()

    st.pyplot(fig)

    st.markdown("""
    In the graph, when the population size drops below the Allee threshold (indicated by the red dashed line), the reproduction rate becomes negative, meaning the population is more likely to decline further rather than recover.
    """)

    # Discussion Questions
    st.subheader("Discussion Questions")
    st.markdown("""
    1. Why do you think species with small populations face such high risks of extinction due to the Allee Effect?
    2. How might factors like habitat fragmentation and human exploitation exacerbate the Allee Effect for certain species?
    3. Which of the vulnerability factors listed above could combine with the Allee Effect to accelerate extinction risk?
    4. How can conservation efforts mitigate the impacts of the Allee Effect on endangered species?
    5. Can you think of examples where a species has been rescued from the Allee Effect through conservation intervention?
    """)

