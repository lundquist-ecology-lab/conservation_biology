import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO

def page4_content():
    # Page Title
    st.title("Understanding Genetic Diversity in Wild Populations")
    
    # Create tabs for the main sections
    main_tabs = st.tabs(["Introduction", "Simulations", "Measurement Methods", "Real-World Examples", "Questions to Consider"])
    
    with main_tabs[0]:  # Introduction tab
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

    with main_tabs[1]:  # Simulations tab
        # Simulation of Genetic Diversity
        st.subheader("Simulation: Visualizing Genetic Diversity")

        # Slider for population size
        population_size = st.slider("Select Population Size", min_value=10, max_value=200, value=50, step=10)

        # Number of different alleles
        num_alleles = st.slider("Select Number of Different Alleles", min_value=2, max_value=10, value=4)

        # Generate random genetic data for initial simulation
        initial_genetic_data = np.random.randint(0, num_alleles, population_size)
        
        # Calculate initial allele frequencies
        initial_frequencies = np.zeros(num_alleles)
        for i in range(num_alleles):
            initial_frequencies[i] = np.sum(initial_genetic_data == i) / population_size
        
        # Create tabs for different views within the simulations tab
        sim_tabs = st.tabs(["Population View", "Genetic Drift Simulation"])
    
        with sim_tabs[0]:
            # Plot initial population
            fig1, ax1 = plt.subplots(figsize=(10, 4))
            
            # Create scatter plot of genetic data
            colors = plt.cm.tab10(initial_genetic_data / max(num_alleles-1, 1))
            ax1.scatter(np.arange(population_size), np.zeros(population_size), c=colors, s=100)
            
            ax1.set_yticks([])
            ax1.set_xticks([])
            ax1.set_title("Genetic Diversity Simulation: Each Circle Represents an Individual")
            
            # Save the plot to a buffer
            buf1 = BytesIO()
            fig1.savefig(buf1, format="png")
            buf1.seek(0)
            image_base64_1 = base64.b64encode(buf1.read()).decode()
            
            # Display plot with custom HTML for 75% width
            html_code_1 = f"""
            <div style="display: flex; justify-content: center; width: 100%; margin-bottom: 20px;">
                <div style="width: 75%;">
                    <img src="data:image/png;base64,{image_base64_1}" style="width: 100%;">
                </div>
            </div>
            """
            st.markdown(html_code_1, unsafe_allow_html=True)
            
            # Show allele frequencies
            st.subheader("Initial Allele Frequencies")
            
            # Plot bar chart of allele frequencies
            fig_freq, ax_freq = plt.subplots(figsize=(10, 4))
            bars = ax_freq.bar(range(num_alleles), initial_frequencies, color=plt.cm.tab10(np.arange(num_alleles) / max(num_alleles-1, 1)))
            ax_freq.set_xlabel("Allele")
            ax_freq.set_ylabel("Frequency")
            ax_freq.set_title("Initial Allele Frequencies")
            ax_freq.set_xticks(range(num_alleles))
            
            # Save the frequency plot to a buffer
            buf_freq = BytesIO()
            fig_freq.savefig(buf_freq, format="png")
            buf_freq.seek(0)
            image_base64_freq = base64.b64encode(buf_freq.read()).decode()
            
            # Display frequency plot
            html_code_freq = f"""
            <div style="display: flex; justify-content: center; width: 100%; margin-bottom: 20px;">
                <div style="width: 75%;">
                    <img src="data:image/png;base64,{image_base64_freq}" style="width: 100%;">
                </div>
            </div>
            """
            st.markdown(html_code_freq, unsafe_allow_html=True)
            
        
        with sim_tabs[1]:
            st.subheader("Genetic Drift Simulation")
            st.write("""
            **Genetic Drift** is a random process that changes allele frequencies in a population due to chance alone. 
            It has a stronger effect in smaller populations, which can lead to:
            - Loss of genetic diversity
            - Fixation (when an allele reaches 100% frequency)
            - Extinction of certain alleles
            - Population bottlenecks and founder effects
            """)
            
            # Control parameters for genetic drift simulation
            col1, col2, col3 = st.columns(3)
            with col1:
                drift_population_size = st.number_input("Population Size", min_value=10, max_value=1000, value=population_size, step=10)
            with col2:
                generations = st.number_input("Number of Generations", min_value=5, max_value=100, value=20, step=5)
            with col3:
                bottleneck_event = st.checkbox("Include Population Bottleneck", value=False)
            
            if bottleneck_event:
                bottleneck_generation = st.slider("Bottleneck at Generation", min_value=5, max_value=generations-2, value=10)
                bottleneck_severity = st.slider("Bottleneck Severity (% surviving)", min_value=5, max_value=50, value=20)
            
            # Simulate genetic drift
            # Initialize array to store allele frequencies over generations
            drift_data = np.zeros((generations, num_alleles))
            
            # Set initial population based on initial frequencies
            population = np.random.choice(num_alleles, drift_population_size, p=initial_frequencies)
            
            # Calculate initial frequencies for drift simulation
            for i in range(num_alleles):
                drift_data[0, i] = np.sum(population == i) / drift_population_size
            
            # Simulate genetic drift over generations
            for gen in range(1, generations):
                # If bottleneck event occurs
                if bottleneck_event and gen == bottleneck_generation:
                    # Determine how many individuals survive the bottleneck
                    survivors_count = int(drift_population_size * bottleneck_severity / 100)
                    # Randomly select survivors
                    survivors_indices = np.random.choice(drift_population_size, survivors_count, replace=False)
                    population = population[survivors_indices]
                    # Restore population size through reproduction (random sampling with replacement)
                    population = np.random.choice(population, drift_population_size, replace=True)
                else:
                    # Normal genetic drift: random sampling with replacement
                    population = np.random.choice(num_alleles, drift_population_size, p=drift_data[gen-1])
                
                # Calculate new frequencies
                for i in range(num_alleles):
                    drift_data[gen, i] = np.sum(population == i) / drift_population_size
            
            # Plot genetic drift over generations
            fig_drift, ax_drift = plt.subplots(figsize=(10, 6))
            for i in range(num_alleles):
                ax_drift.plot(range(generations), drift_data[:, i], 
                             label=f"Allele {i}", 
                             color=plt.cm.tab10(i / max(num_alleles-1, 1)), 
                             linewidth=2)
            
            # Add vertical line for bottleneck event
            if bottleneck_event:
                ax_drift.axvline(x=bottleneck_generation, color='red', linestyle='--', alpha=0.7, 
                               label=f"Bottleneck ({bottleneck_severity}% survived)")
            
            ax_drift.set_xlabel("Generation")
            ax_drift.set_ylabel("Allele Frequency")
            ax_drift.set_title("Genetic Drift Simulation: Allele Frequencies Over Time")
            ax_drift.legend(loc="center left", bbox_to_anchor=(1, 0.5))
            ax_drift.grid(True, alpha=0.3)
            
            # Save the drift plot to a buffer
            buf_drift = BytesIO()
            fig_drift.tight_layout()
            fig_drift.savefig(buf_drift, format="png")
            buf_drift.seek(0)
            image_base64_drift = base64.b64encode(buf_drift.read()).decode()
            
            # Display drift plot
            html_code_drift = f"""
            <div style="display: flex; justify-content: center; width: 100%; margin-bottom: 20px;">
                <div style="width: 85%;">
                    <img src="data:image/png;base64,{image_base64_drift}" style="width: 100%;">
                </div>
            </div>
            """
            st.markdown(html_code_drift, unsafe_allow_html=True)
            
            # Final population visualization after drift
            st.subheader("Final Population After Genetic Drift")
            final_population = np.random.choice(num_alleles, drift_population_size, p=drift_data[-1])
            
            fig_final, ax_final = plt.subplots(figsize=(10, 4))
            colors_final = plt.cm.tab10(final_population / max(num_alleles-1, 1))
            ax_final.scatter(np.arange(drift_population_size), np.zeros(drift_population_size), c=colors_final, s=100)
            ax_final.set_yticks([])
            ax_final.set_xticks([])
            ax_final.set_title("Final Population After Genetic Drift")
            
            # Save the final population plot to a buffer
            buf_final = BytesIO()
            fig_final.savefig(buf_final, format="png")
            buf_final.seek(0)
            image_base64_final = base64.b64encode(buf_final.read()).decode()
            
            # Display final population plot
            html_code_final = f"""
            <div style="display: flex; justify-content: center; width: 100%; margin-bottom: 20px;">
                <div style="width: 75%;">
                    <img src="data:image/png;base64,{image_base64_final}" style="width: 100%;">
                </div>
            </div>
            """
            st.markdown(html_code_final, unsafe_allow_html=True)
            
            # Calculate and display diversity metrics
            initial_diversity = 1 - sum([freq**2 for freq in initial_frequencies])
            final_diversity = 1 - sum([freq**2 for freq in drift_data[-1]])
            diversity_change = ((final_diversity - initial_diversity) / initial_diversity) * 100
            
            st.subheader("Genetic Diversity Metrics")
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Initial Diversity Index", f"{initial_diversity:.3f}")
            col2.metric("Final Diversity Index", f"{final_diversity:.3f}")
            col3.metric("Change in Diversity", f"{diversity_change:.1f}%", 
                      delta_color="normal" if diversity_change >= 0 else "inverse")
            
            st.write("""
            **Diversity Index** used here is a variant of Nei's genetic diversity index (1 - sum of squared frequencies),
            which measures the probability that two randomly selected alleles from the population will be different.
            Higher values indicate greater genetic diversity.
            """)
            
            # Key observations and explanations
            st.subheader("Key Observations")
            st.write("""
            This simulation demonstrates several important concepts in population genetics:
            
            1. **Genetic Drift's Impact on Small Populations**: Notice how smaller populations show more dramatic changes in allele frequencies over time due to random chance events.
            
            2. **Loss of Alleles**: Some alleles may completely disappear from the population, particularly in smaller populations or after bottleneck events. Once an allele is lost, it cannot return without mutation or migration.
            
            3. **Fixation**: Some alleles may reach 100% frequency (fixation), eliminating all other genetic variants at that locus.
            
            4. **Bottleneck Effects**: Population bottlenecks dramatically accelerate genetic drift and can cause rapid loss of genetic diversity.
            
            5. **Conservation Implications**: This demonstrates why maintaining large, connected populations is crucial for conserving genetic diversity in endangered species.
            """)

            # Add a Monte Carlo simulation button to run multiple iterations
            st.subheader("Long-term Diversity Loss Analysis")
            
            if st.button("Run 1000 Simulations"):
                with st.spinner("Running simulations..."):
                    # Parameters for the Monte Carlo simulation
                    mc_population_size = drift_population_size
                    mc_num_alleles = num_alleles
                    mc_iterations = 1000
                    mc_generations = 20
                    
                    # Array to store diversity changes
                    diversity_changes = np.zeros(mc_iterations)
                    
                    # Run the simulations
                    for i in range(mc_iterations):
                        # Initial population with equal allele frequencies
                        mc_initial_frequencies = np.ones(mc_num_alleles) / mc_num_alleles
                        initial_diversity = 1 - sum([freq**2 for freq in mc_initial_frequencies])
                        
                        # Initialize population
                        population = np.random.choice(mc_num_alleles, mc_population_size, p=mc_initial_frequencies)
                        
                        # Run for mc_generations
                        for gen in range(mc_generations):
                            # Simple genetic drift: random sampling with replacement
                            current_freq = np.zeros(mc_num_alleles)
                            for j in range(mc_num_alleles):
                                current_freq[j] = np.sum(population == j) / mc_population_size
                            
                            population = np.random.choice(mc_num_alleles, mc_population_size, p=current_freq)
                        
                        # Calculate final frequencies
                        final_freq = np.zeros(mc_num_alleles)
                        for j in range(mc_num_alleles):
                            final_freq[j] = np.sum(population == j) / mc_population_size
                        
                        # Calculate final diversity
                        final_diversity = 1 - sum([freq**2 for freq in final_freq])
                        
                        # Store diversity change percentage
                        diversity_changes[i] = ((final_diversity - initial_diversity) / initial_diversity) * 100
                    
                    # Calculate statistics
                    avg_diversity_change = np.mean(diversity_changes)
                    median_diversity_change = np.median(diversity_changes)
                    min_diversity_change = np.min(diversity_changes)
                    max_diversity_change = np.max(diversity_changes)
                    
                    # Display results
                    st.subheader("Results from 1000 Simulations")
                    
                    col1, col2, col3, col4 = st.columns(4)
                    col1.metric("Average Diversity Change", f"{avg_diversity_change:.2f}%", 
                              delta_color="normal" if avg_diversity_change >= 0 else "inverse")
                    col2.metric("Median Diversity Change", f"{median_diversity_change:.2f}%")
                    col3.metric("Min Diversity Change", f"{min_diversity_change:.2f}%")
                    col4.metric("Max Diversity Change", f"{max_diversity_change:.2f}%")
                    
                    # Plot histogram of diversity changes
                    fig_hist, ax_hist = plt.subplots(figsize=(10, 6))
                    ax_hist.hist(diversity_changes, bins=30, alpha=0.7, color='blue')
                    ax_hist.axvline(x=avg_diversity_change, color='red', linestyle='--', 
                                   label=f"Average: {avg_diversity_change:.2f}%")
                    ax_hist.set_xlabel("Diversity Change (%)")
                    ax_hist.set_ylabel("Frequency")
                    ax_hist.set_title("Distribution of Diversity Changes After 20 Generations")
                    ax_hist.legend()
                    ax_hist.grid(True, alpha=0.3)
                    
                    # Save the histogram plot to a buffer
                    buf_hist = BytesIO()
                    fig_hist.tight_layout()
                    fig_hist.savefig(buf_hist, format="png")
                    buf_hist.seek(0)
                    image_base64_hist = base64.b64encode(buf_hist.read()).decode()
                    
                    # Display histogram plot
                    html_code_hist = f"""
                    <div style="display: flex; justify-content: center; width: 100%; margin-bottom: 20px;">
                        <div style="width: 85%;">
                            <img src="data:image/png;base64,{image_base64_hist}" style="width: 100%;">
                        </div>
                    </div>
                    """
                    st.markdown(html_code_hist, unsafe_allow_html=True)
                    
                    # Calculate how often an allele was lost completely
                    allele_loss_count = 0
                    for i in range(mc_iterations):
                        final_pop = np.random.choice(mc_num_alleles, mc_population_size, 
                                                 p=np.ones(mc_num_alleles)/mc_num_alleles)
                        for gen in range(mc_generations):
                            current_freq = np.zeros(mc_num_alleles)
                            for j in range(mc_num_alleles):
                                current_freq[j] = np.sum(final_pop == j) / mc_population_size
                            
                            final_pop = np.random.choice(mc_num_alleles, mc_population_size, p=current_freq)
                        
                        # Count iterations where at least one allele was lost
                        final_freqs = np.zeros(mc_num_alleles)
                        for j in range(mc_num_alleles):
                            final_freqs[j] = np.sum(final_pop == j) / mc_population_size
                        
                        if np.any(final_freqs == 0):
                            allele_loss_count += 1
                    
                    allele_loss_percentage = (allele_loss_count / mc_iterations) * 100
                    
                    st.metric("Probability of Allele Loss", f"{allele_loss_percentage:.1f}%", 
                            help="Percentage of simulations where at least one allele was completely lost")
                    
                    st.write("""
                    This Monte Carlo simulation shows the long-term impacts of genetic drift across many possible scenarios.
                    The negative average diversity change demonstrates how genetic drift consistently reduces genetic diversity 
                    over time, particularly in small populations.
                    """)
    
    with main_tabs[2]:  # Measurement Methods tab
        # Measures of Genetic Diversity
        st.subheader("How is Genetic Diversity Measured?")
        st.write("""
        There are several ways to measure genetic diversity in wild populations:
        - **Allelic Richness**: The total number of different alleles present in a population.
        - **Heterozygosity**: The proportion of individuals in a population that have two different alleles at a particular gene locus.
        - **Genetic Distance**: A measure of the genetic difference between populations, often used to study the evolutionary relationships between species.
        - **Genomic Methods**: Modern genomic techniques such as SNP (Single Nucleotide Polymorphism) analysis and whole-genome sequencing allow for comprehensive assessments of genetic diversity at a very fine scale.
        """)

    with main_tabs[3]:  # Real-World Examples tab
        # Example: Genetic Diversity in Wild Populations
        st.subheader("Genetic Diversity in Wild Populations")
        st.write("""
        Let's consider examples of genetic diversity in wild populations:

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
        
    with main_tabs[4]:  # Questions to Consider tab
        st.subheader("Questions to Consider")
        st.write("""
        1. How does population size affect the rate and severity of genetic drift?
        2. What happens to rare alleles during genetic drift? Why does this matter for conservation?
        3. How does a population bottleneck affect genetic diversity compared to normal genetic drift?
        4. Why is maintaining genetic diversity particularly important for species facing environmental changes or disease outbreaks?
        5. Based on the simulation results, what minimum population size would you recommend for maintaining genetic diversity in an endangered species?
        6. How might the introduction of individuals from different populations (gene flow) counteract the effects of genetic drift?
        7. Compare the genetic diversity loss in small versus large populations. What patterns do you observe?
        8. What conservation strategies might help preserve genetic diversity in isolated wildlife populations?
        """)
        
        st.write("""
        **Original Question**: If you set alleles to 2 and shift between 10 and 20 individuals, what
        happens to the relative abundance of each allele? Why might this be an
        issue in small populations?
        """)
