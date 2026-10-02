import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def page4_content():
    # Title and credits
    st.title("Biomagnification Lab")
    st.markdown("Credit: [PennState Extension](https://extension.psu.edu/biomagnification-activity)")

    # Introduction
    st.markdown("""
    **Learning Objective:**
    This activity simulates biomagnification, a process where organisms accumulate chemical residues from the organisms they consume in the food chain.
    """)

    # Explanation of Biomagnification
    st.header("What is Biomagnification?")
    st.markdown("""
    Biomagnification occurs when organisms accumulate chemical residues from the organisms they consume, leading to higher chemical concentrations in animals higher up the food chain.
    """)
    
    # Example
    st.header("Example: Mercury (Hg) in the oceans")
    
    st.write("""
             Mercury, (specifically monomethylmercury), is a neurotoxin that is known to 
             biomagnify in ocean food webs. Mercury is typically found in the atmosphere and the amount
             of Hg in the atmosphere has increased due to anthropogenic emissions. The 
             plot below by Zhang et al. (2020) shows a model of Hg concentrations in
             phytoplankton and zooplankton around the world. According to Zang et al. (2020),
             high concentrations in the 
             poles is likely due to low temperature and low solar radiation. High concentrations
             near the equator are likely due to increased microbial metabolism and 
             atmospheric deposition.
             
             Mercury in plankton then is consumed by small fish, which are then consumed
             by larger fish. As trophic levels increase, the concentration of 
             Hg in their tissue. This is a major global health issue due to the fact
             that more than 35% of the worlds population relies on seafood as their 
             primary source of protein (World Wildlife Fund 2024).
             
             """)
    col1, col2 = st.columns([1, 1])  # The first column is twice as wide as the second

    with col1:
        st.image("https://agupubs.onlinelibrary.wiley.com/cms/asset/7da1d7c4-78d0-4fe5-9dd0-4000d1e24a9e/gbc20954-fig-0006-m.jpg")
        st.markdown("Source: [Zhang et al. (2020)](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2019GB006348)")
    with col2:
        st.image('./unit4/images/hg_fish.png')
        st.markdown("Source: [US FDA](https://www.fda.gov/media/102331/download?attachment)")
    
    # Activity Setup
    st.header("The Food Chain Simulation")
    st.markdown("""
    In this simulation, you'll see how contamination in a water body gets passed up the food chain:
    - **P:** Planktonic algae with 0.5 ppm (parts per million) of chemical from the water.
    - **Z:** Zooplankton, which eat the algae.
    - **F:** Fish, which eat the zooplankton.
    - **B:** Bird, which eats the fish.

    Follow the steps below to see how the concentration increases as we go up the food chain!
    """)

     # Step 1: Planktonic Algae
    st.subheader("Step 1: Algae")
    st.markdown("Start with algae, which have absorbed **0.5 ppm** of the chemical from the water.")
    num_algae = st.slider("How many algal cells are in the ecosystem?", 1, 10000, 1000)

    col1, col2 = st.columns([2, 1])  # The first column is twice as wide as the second

    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/%D0%92%D0%BE%D0%B4%D0%BE%D1%80%D0%BE%D1%81%D0%BB%D0%B8_%D0%BF%D1%80%D0%B5%D1%81%D0%BD%D0%BE%D0%B2%D0%BE%D0%B4%D0%BD%D0%BE%D0%B3%D0%BE_%D0%B2%D0%BE%D0%B4%D0%BE%D0%B5%D0%BC%D0%B0_2.jpg/1024px-%D0%92%D0%BE%D0%B4%D0%BE%D1%80%D0%BE%D1%81%D0%BB%D0%B8_%D0%BF%D1%80%D0%B5%D1%81%D0%BD%D0%BE%D0%B2%D0%BE%D0%B4%D0%BD%D0%BE%D0%B3%D0%BE_%D0%B2%D0%BE%D0%B4%D0%BE%D0%B5%D0%BC%D0%B0_2.jpg")
        
    # Step 2: Zooplankton eat algae
    st.subheader("Step 2: Zooplankton")
    num_zooplankton = st.slider("How many individual zooplankton will eat algae?", 1, 1000, 100)
    algae_eaten_per_zooplankton = st.slider("How many algae does each zooplankton eat?", 1, 50, 10)
    total_algae_concentration = algae_eaten_per_zooplankton * 0.5  # Each zooplankton consumes algae

    st.write(f"Each zooplankton now contains {total_algae_concentration} ppm of chemicals.")

    col1, col2 = st.columns([2, 1])  # The first column is twice as wide as the second

    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/4/4e/Daphnia_pulex.png")
    
    # Step 3: Fish eat zooplankton
    st.subheader("Step 3: Fish")
    num_fish = st.slider("How many fish will eat the zooplankton?", 1, 100, 10)
    zooplankton_eaten_per_fish = st.slider("How many zooplankton does each fish eat?", 1, 50, 10)
    total_fish_concentration = zooplankton_eaten_per_fish * total_algae_concentration

    st.write(f"Each fish now contains {total_fish_concentration} ppm of chemicals.")
    
    col1, col2 = st.columns([2, 1])  # The first column is twice as wide as the second

    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Lake_trout_fish_in_hands_salvelinus_namaycush.jpg/1920px-Lake_trout_fish_in_hands_salvelinus_namaycush.jpg")

    # Step 4: Birds eat fish
    st.subheader("Step 4: Birds")
    num_birds = st.slider("How many birds will eat the fish?", 1, 10, 1)
    fish_eaten_per_bird = st.slider("How many fish does each bird eat?", 1, 10, 2)
    total_bird_concentration = fish_eaten_per_bird * total_fish_concentration

    st.write(f"Each bird now contains {total_bird_concentration} ppm of chemicals.")
    
    col1, col2 = st.columns([2, 1])  # The first column is twice as wide as the second

    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Bald_eagle_about_to_fly_in_Alaska_%282016%29.jpg/1280px-Bald_eagle_about_to_fly_in_Alaska_%282016%29.jpg")
    
    # Pyramid Visualization
    st.header("Biomagnification Pyramid")
    st.markdown("The following pyramid shows how the concentration of chemicals increases as we go up the food chain.")

    # Data for the pyramid
    levels = ["Bird", "Fish", "Zooplankton", "Algae"]
    ppm_values = [total_bird_concentration, total_fish_concentration, total_algae_concentration, 0.5]

    fig, ax = plt.subplots(figsize=(6, 8))

    # Create an upside-down pyramid
    for i, (level, ppm) in enumerate(zip(levels, ppm_values)):
        ax.fill_between(
            [i, i + 1], 
            [-ppm] * 2, 
            [0] * 2, 
            label=f"{level}: {ppm:.2f} ppm", 
            edgecolor='black'
        )

    ax.set_xlim(0, 4)
    ax.set_ylim(-max(ppm_values), 0)
    ax.set_xticks(np.arange(4) + 0.5)
    ax.set_xticklabels(levels)
    ax.set_yticklabels([])
    ax.legend()

    ax.set_title("Biomagnification Pyramid")
    ax.set_xlabel("Trophic Level")
    ax.set_ylabel("Parts Per Million (ppm)")

    st.pyplot(fig)
    
    # Conclusion
    st.header("Conclusion")
    st.markdown(f"""
    As you can see, even though each algae only started with 0.5 ppm of chemical, the bird at the top of the food chain now has **{total_bird_concentration} ppm** of the chemical in its body.

    This illustrates how biomagnification works: chemicals accumulate and magnify as they move up the food chain!
    """)
    
    # Questions
    st.header("Questions")
    
    st.markdown("""
    1. **How does biomagnification affect species at the top of the food chain?**  
       Considering the bird in this activity, what long-term impacts might such high chemical concentrations have on its health and reproduction?

    2. **If humans are at the top of some food chains, how might biomagnification impact human populations?**  
       Can you think of any real-world examples where biomagnification of pollutants or chemicals has affected human communities?

    3. **What strategies could be used to reduce biomagnification in ecosystems?**  
       Think about how agricultural practices, industrial processes, or environmental regulations could be adjusted to limit chemical accumulation in the environment.

    4. **Why is biomagnification a concern even if the chemical concentration in the environment (e.g., water) is very low?**  
       How does the process of biomagnification explain why even small amounts of a contaminant can become dangerous over time?
    """)