import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import seaborn as sns
from scipy.stats import norm
import plotly.express as px

def create_population_simulation(initial_pop, years, survival_prob):
    populations = []
    current_pop = initial_pop
    
    for _ in range(years):
        if np.random.random() < survival_prob:
            # Random variation in population growth (-10% to +20%)
            growth_rate = np.random.uniform(0.9, 1.2)
            current_pop = int(current_pop * growth_rate)
        else:
            # Population decline event (-20% to -40%)
            decline_rate = np.random.uniform(0.6, 0.8)
            current_pop = int(current_pop * decline_rate)
        populations.append(current_pop)
    
    return populations

def calculate_mvp_probability(population_size):
    """Calculate probability of population persistence based on size."""
    # Simplified model using logistic function
    k = 0.01  # Steepness of the curve
    x0 = 250  # Population size at 50% probability
    return 1 / (1 + np.exp(-k * (population_size - x0)))

# MVP calculation function
def calculate_mvp(r, sd, p_survival, time_years):
    """
    Calculate Minimum Viable Population using demographic stochasticity
    with corrections for high growth rates and minimum population constraints
    
    Parameters:
    r: growth rate
    sd: environmental variability
    p_survival: probability of survival (1 - p_extinction)
    time_years: time horizon
    """
    z = norm.ppf(p_survival)  # z-score for desired survival probability
    
    # Add demographic stochasticity term
    demo_term = 1 / (2 * r) if r > 0 else 1
    
    # Calculate MVP with both environmental and demographic stochasticity
    mvp = np.exp((0.5 * sd**2 - r) * time_years + z * sd * np.sqrt(time_years)) + demo_term
    
    # Apply minimum threshold - no population can be less than 50
    # This accounts for genetic diversity requirements
    mvp = max(50, mvp)
    
    return int(np.ceil(mvp))

def page0_content():
    st.title("Applied Conservation Biology")
    
    # Sidebar with navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Data Types", "Data Collection Methods", "PVA and MVP", "MDA and Metapopulations", "Extinction Debt"])
    
    if page == "Data Types":
        # Key Information Section
        st.header("Types of data to collect")
        
        with st.expander("Population Demographics"):
            st.markdown("""
            - Population size and density
            - Age structure and sex ratios
            - Birth rates and death rates
            - Immigration and emigration rates
            - Growth rates and population trends
            """)
            
        with st.expander("Habitat Requirements"):
            st.markdown("""
            - Geographic range and distribution
            - Habitat type preferences
            - Resource requirements
            - Territory size
            - Seasonal movement patterns
            """)
            
        with st.expander("Behavioral Patterns"):
            st.markdown("""
            - Social structure
            - Mating systems
            - Foraging behavior
            - Daily activity patterns
            - Seasonal behavioral changes
            """)
            
        with st.expander("Environmental Interactions"):
            st.markdown("""
            - Predator-prey relationships
            - Competition with other species
            - Symbiotic relationships
            - Response to environmental changes
            - Human-wildlife conflicts
            """)
    
    # Types of Studies Section
    elif page == "Data Collection Methods":
        st.header("Common Research Methods in Conservation Biology")
        
        study_types = {
            "Mark-Recapture Studies": "Involves capturing, marking, and releasing animals to estimate population size and survival rates.",
            "Radio Telemetry": "Tracking individual animals using radio collars or tags to understand movement patterns and habitat use.",
            "Genetic Studies": "Analysis of DNA to understand population structure, genetic diversity, and gene flow.",
            "Camera Trap Surveys": "Using motion-activated cameras to study species presence, abundance, and behavior.",
            "Habitat Assessment": "Evaluating vegetation structure, food availability, and environmental conditions.",
        }
        
        for study, description in study_types.items():
            with st.expander(study):
                st.write(description)
    
        st.markdown("""
        
        **Monitoring**, particularly long-term monitoring is essential for understanding natural populations. By tracking populations, behaviors, and ecosystems over years or 
        decades, scientists can detect subtle changes that might be missed in shorter studies, distinguish between natural fluctuations and 
        concerning declines, and identify emerging threats before they become critical. This sustained observation helps researchers understand 
        species' responses to environmental changes, evaluate the success of conservation efforts, and adapt management strategies accordingly.
        
        
        """)
    elif page == "PVA and MVP":
    
        # Population Viability Analysis Section
        st.header("Population Viability Analysis (PVA)")
        
        st.markdown("""
        PVA is a species-specific method used to estimate the likelihood that a population will persist for a given time into the future. 
        It considers factors such as:
        - Demographic stochasticity
        - Environmental variation
        - Genetic factors
        - Catastrophic events
        """)
        
        # Interactive PVA Simulation
        st.subheader("PVA Simulation Example")
        
        col1, col2 = st.columns(2)
        
        with col1:
            initial_population = st.slider("Initial Population Size", 50, 500, 200)
            simulation_years = st.slider("Simulation Years", 10, 100, 50)
        
        # Generate example data
        np.random.seed(42)  # For reproducibility
        
        # Run multiple simulations
        n_simulations = 100
        high_survival_data = []
        low_survival_data = []
        
        for _ in range(n_simulations):
            high_survival_data.append(create_population_simulation(initial_population, simulation_years, 0.9))
            low_survival_data.append(create_population_simulation(initial_population, simulation_years, 0.5))
        
        # Calculate mean populations
        high_survival_mean = np.mean(high_survival_data, axis=0)
        low_survival_mean = np.mean(low_survival_data, axis=0)
        
        # Plotting PVA
        fig, ax = plt.subplots(figsize=(10, 6))
        years = range(simulation_years)
        
        ax.plot(years, high_survival_mean, label='90% Survival Probability', color='green')
        ax.plot(years, low_survival_mean, label='50% Survival Probability', color='red')
        
        # Add confidence intervals
        high_percentile_upper = np.percentile(high_survival_data, 95, axis=0)
        high_percentile_lower = np.percentile(high_survival_data, 5, axis=0)
        low_percentile_upper = np.percentile(low_survival_data, 95, axis=0)
        low_percentile_lower = np.percentile(low_survival_data, 5, axis=0)
        
        ax.fill_between(years, high_percentile_lower, high_percentile_upper, alpha=0.2, color='green')
        ax.fill_between(years, low_percentile_lower, low_percentile_upper, alpha=0.2, color='red')
        
        ax.set_xlabel('Years')
        ax.set_ylabel('Population Size')
        ax.set_title('Population Viability Analysis Simulation')
        ax.legend()
        ax.grid(True)
        
        st.pyplot(fig)
        
        # Minimum Viable Population Section
        st.header("Minimum Viable Population (MVP)")
        
        st.markdown("""
        MVP is the smallest isolated population having a 99% chance of surviving for 1000 years. Factors affecting MVP:
        
        1. **Genetic Considerations:**
        - Maintaining genetic diversity
        - Avoiding inbreeding depression
        
        2. **Demographic Considerations:**
        - Birth and death rates
        - Sex ratio
        - Age structure
        
        3. **Environmental Considerations:**
        - Habitat quality
        - Resource availability
        - Natural disasters
        
        4. **Spatial Considerations:**
        - Habitat fragmentation
        - Connectivity between populations
        """)

        # MVP Interactive Graph
        st.subheader("MVP Probability Graph")
        
        # Generate data for MVP graph
        pop_sizes = np.linspace(0, 500, 100)
        probabilities = [calculate_mvp_probability(size) for size in pop_sizes]
        
        # Create MVP visualization
        fig_mvp, ax_mvp = plt.subplots(figsize=(10, 6))
        ax_mvp.plot(pop_sizes, probabilities, 'b-', linewidth=2)
        
        # Customize the plot
        ax_mvp.set_xlabel('Population Size')
        ax_mvp.set_ylabel('Probability of Population Persistence')
        ax_mvp.set_title('Minimum Viable Population Probability Curve')
        ax_mvp.grid(True)
        ax_mvp.legend()
        
        # Add shaded regions for different risk categories
        ax_mvp.fill_between(pop_sizes, probabilities, 1, alpha=0.1, color='green', label='Low Risk')
        ax_mvp.fill_between(pop_sizes, 0, probabilities, alpha=0.1, color='red', label='High Risk')
        
        st.pyplot(fig_mvp)
        
        st.markdown("""
        ### Understanding the MVP Graph
        
        The graph above shows the relationship between population size and the probability of long-term persistence:
        
        The curve demonstrates that:
        1. Very small populations have a low probability of persistence
        2. The probability increases rapidly within a critical range
        3. Beyond a certain population size, additional individuals provide diminishing returns in terms of survival probability
        """)
        
    elif page == "MDA and Metapopulations":
        
        st.markdown("""
        ---
        ## Minimum Dynamic Area (MDA) and Metapopulation Dynamics

        ### Minimum Dynamic Area
        The Minimum Dynamic Area (MDA) is the smallest area of suitable habitat needed to maintain a viable population. It's calculated as:

        $MDA = \\frac{MVP}{D}$

        Where:
        - MVP = Minimum Viable Population
        - D = Population density (individuals per unit area)

        However, this basic equation needs to be modified for:
        1. Edge effects
        2. Habitat heterogeneity
        3. Disturbance regimes
        """)

        # Calculate sample MVPs for current parameters
        st.subheader("Population Parameters")
        param_cols = st.columns(2)
        with param_cols[0]:
            r = st.slider("Growth rate (r)", 0.01, 0.3, 0.1, 0.01,
                        help="Average population growth rate per year")
        with param_cols[1]:
            sd = st.slider("Environmental variability (σ)", 0.1, 1.0, 0.3, 0.05,
                        help="Standard deviation of growth rate")

        # Now calculate MVPs with the defined parameters
        sample_times = [50, 100, 200, 500]
        mvp_data = {
            'Time Horizon (Years)': sample_times,
            'MVP (90% Survival)': [calculate_mvp(r, sd, 0.90, t) for t in sample_times],
            'MVP (50% Survival)': [calculate_mvp(r, sd, 0.50, t) for t in sample_times]
        }

        # Add density slider for MDA calculation
        st.subheader("Explore MDA Requirements")
        density = st.slider("Population density (individuals per km²)", 0.1, 10.0, 1.0, 0.1,
                        help="Average number of individuals per square kilometer")

        # Calculate MDA using the last (longest time horizon) MVP values
        mda_90 = mvp_data['MVP (90% Survival)'][-1] / density
        mda_50 = mvp_data['MVP (50% Survival)'][-1] / density

        mda_cols = st.columns(2)
        with mda_cols[0]:
            st.metric("MDA for 90% Survival", f"{mda_90:.1f} km²")
        with mda_cols[1]:
            st.metric("MDA for 50% Survival", f"{mda_50:.1f} km²")

        # Create a table of MVPs and corresponding MDAs
        mda_table_data = {
            'Time Horizon (Years)': sample_times,
            'MVP (90% Survival)': mvp_data['MVP (90% Survival)'],
            'MDA (90% Survival) km²': [mvp/density for mvp in mvp_data['MVP (90% Survival)']],
            'MVP (50% Survival)': mvp_data['MVP (50% Survival)'],
            'MDA (50% Survival) km²': [mvp/density for mvp in mvp_data['MVP (50% Survival)']]
        }
        mda_df = pd.DataFrame(mda_table_data)

        st.subheader("MVP and MDA Values Over Time")
        st.table(mda_df.round(1))

        st.markdown("---")
        st.header("Metapopulation Theory and Applications")

        # Structure and Management sections
        structure_cols = st.columns(2)
        with structure_cols[0]:
            st.markdown("""
            #### Structure Components
            1. **Habitat Patches**
                - Size and quality variation
                - Spatial distribution
                - Edge effects
                
            2. **Connectivity**
                - Dispersal corridors
                - Matrix habitat quality
                - Distance between patches
                
            3. **Population Processes**
                - Local extinction
                - Recolonization
                - Source-sink dynamics
            """)

        with structure_cols[1]:
            st.markdown("""
            #### Management Implications
            1. **Network Design**
                - Optimal patch size
                - Patch spacing
                - Corridor width
                
            2. **Population Viability**
                - Rescue effects
                - Genetic connectivity
                - Risk spreading
                
            3. **Conservation Strategies**
                - Habitat restoration
                - Corridor protection
                - Population augmentation
            """)

        # Metapopulation visualization
        def create_metapopulation_diagram():
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.set_xlim(0, 10)
            ax.set_ylim(0, 6)
            
            # Create patches of different sizes
            patches_data = [
                (2, 4, 0.8, 'Source'),  # x, y, size, type
                (5, 3, 0.6, 'Sink'),
                (8, 4, 0.7, 'Source'),
                (3, 1.5, 0.5, 'Sink'),
                (7, 1.5, 0.6, 'Sink')
            ]
            
            # Draw patches
            for x, y, size, type in patches_data:
                circle = plt.Circle((x, y), size, 
                                color='forestgreen' if type == 'Source' else 'lightgreen',
                                alpha=0.6)
                ax.add_patch(circle)
                
                # Label patches
                ax.text(x, y, type, ha='center', va='center')
            
            # Draw arrows for dispersal (corrected to only go from sources to sinks)
            arrows = [
                (2.8, 4, 4.4, 3.2),    # Source 1 to Sink 1
                (8, 4, 7, 2.1),        # Source 2 to Sink 3
                (2.3, 3.2, 3, 2),      # Source 1 to Sink 2
                (8, 3.8, 5.6, 3)       # Source 2 to Sink 1
            ]
            
            for x1, y1, x2, y2 in arrows:
                ax.arrow(x1, y1, x2-x1, y2-y1, 
                        head_width=0.1, head_length=0.2, 
                        fc='gray', ec='gray', alpha=0.5)
            
            ax.set_title('Metapopulation Structure: Source-Sink Dynamics')
            ax.set_xticks([])
            ax.set_yticks([])
            
            return fig

        st.subheader("Metapopulation Visualization")
        st.pyplot(create_metapopulation_diagram())

        st.markdown("""
        ### Levins' Metapopulation Model

        The classic Levins' model describes metapopulation dynamics:

        $\\frac{dp}{dt} = mp(1-p) - ep$

        Where:
        - p = proportion of occupied patches
        - m = colonization rate
        - e = extinction rate

        #### Key Thresholds:
        1. **Persistence Threshold**: m/e > 1
        2. **Minimum Habitat**: proportion of suitable habitat > e/m

        ### Practical Applications

        1. **Reserve Design**
        - Multiple smaller reserves may be better than single large reserve
        - Need to ensure adequate connectivity
        - Balance between patch size and number of patches

        2. **Management Strategies**
        - Maintain or restore habitat corridors
        - Protect source populations
        - Monitor population connectivity
        - Manage matrix habitat

        3. **Risk Assessment**
        - Consider both local and regional extinction risks
        - Evaluate corridor effectiveness
        - Assess patch quality and connectivity
        """)

        # Add interactive metapopulation stability calculator
        st.markdown("---")
        st.subheader("Metapopulation Stability Calculator")

        calculator_cols = st.columns(2)
        with calculator_cols[0]:
            m_rate = st.slider("Colonization rate (m)", 0.0, 1.0, 0.3, 0.1)
        with calculator_cols[1]:
            e_rate = st.slider("Extinction rate (e)", 0.0, 1.0, 0.1, 0.1)

        stability_ratio = m_rate/e_rate
        min_habitat = e_rate/m_rate if m_rate > 0 else float('inf')

        metric_cols = st.columns(2)
        with metric_cols[0]:
            st.metric("Persistence Ratio (m/e)", f"{stability_ratio:.2f}",
                    delta="Stable" if stability_ratio > 1 else "Unstable")
        with metric_cols[1]:
            st.metric("Minimum Habitat Required", f"{min_habitat:.1%}")
            
    elif page == "Extinction Debt":
        def calculate_extinction_debt(initial_species, habitat_loss_rate, years):
            """Calculate species loss over time including extinction debt effects"""
            time = np.linspace(0, years, years+1)
            habitat_remaining = 100 * (1 - habitat_loss_rate) ** time
            
            # Calculate expected equilibrium species based on species-area relationship
            z = 0.25  # typical z-value for species-area relationship
            expected_species = initial_species * (habitat_remaining/100) ** z
            
            # Calculate actual species with time lag (extinction debt)
            # Using a simple exponential decay towards expected species
            relaxation_rate = 0.1
            actual_species = np.zeros(len(time))
            actual_species[0] = initial_species
            
            for t in range(1, len(time)):
                # Simple difference equation instead of differential equation
                diff = actual_species[t-1] - expected_species[t-1]
                actual_species[t] = actual_species[t-1] - relaxation_rate * diff
            
            return pd.DataFrame({
                'Year': time,
                'Habitat_Remaining_%': habitat_remaining,
                'Expected_Species': expected_species,
                'Actual_Species': actual_species
            })

        st.title("Extinction Debt")
        st.write("""
        This interactive tool helps you understand the concept of extinction debt in conservation biology. 
        Extinction debt refers to the future extinctions that will occur due to past habitat destruction, 
        even if no further habitat is lost.
        """)

        # Sidebar controls
        st.sidebar.header("Simulation Parameters")
        initial_species = st.sidebar.slider("Initial Number of Species", 100, 1000, 500)
        habitat_loss_rate = st.sidebar.slider("Annual Habitat Loss Rate (%)", 0.0, 5.0, 1.0) / 100
        simulation_years = st.sidebar.slider("Simulation Years", 10, 100, 50)

        # Generate data
        df = calculate_extinction_debt(initial_species, habitat_loss_rate, simulation_years)

        # Main content
        col1, col2 = st.columns([2, 1])

        with col1:
            st.subheader("Extinction Debt Visualization")
            
            fig = px.line(df, x='Year', y=['Expected_Species', 'Actual_Species', 'Habitat_Remaining_%'],
                        title='Species Loss and Habitat Change Over Time')
            fig.update_layout(
                yaxis_title="Number of Species / Habitat Remaining (%)",
                hovermode='x unified'
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("Key Metrics")
            current_debt = df['Actual_Species'].iloc[-1] - df['Expected_Species'].iloc[-1]
            
            st.metric("Current Extinction Debt", 
                    f"{int(abs(current_debt))} species",
                    f"{'Surplus' if current_debt > 0 else 'Deficit'}")
            
            st.metric("Habitat Remaining", 
                    f"{df['Habitat_Remaining_%'].iloc[-1]:.1f}%",
                    f"-{habitat_loss_rate*100:.1f}% annually")
            
            st.metric("Species Remaining", 
                    f"{int(df['Actual_Species'].iloc[-1])} species",
                    f"{((df['Actual_Species'].iloc[-1]/initial_species)-1)*100:.1f}% from initial")

        # Educational content
        st.markdown("""
        ### Understanding Extinction Debt

        Extinction debt is a crucial concept in conservation biology that describes the delayed extinction 
        of species following habitat loss. This delay occurs because:

        1. **Population Dynamics**: Species may persist for some time even in suboptimal conditions
        2. **Metapopulation Effects**: Connected populations may temporarily sustain each other
        3. **Generation Time**: Long-lived species may take several generations to show effects

        ### How to Use This Tool

        - Adjust the parameters in the sidebar to explore different scenarios
        - Compare the blue line (actual species) with the orange line (expected species)
        - The gap between these lines represents the extinction debt
        - The green line shows habitat loss over time

        ### Important Considerations

        - The model uses a simplified version of species-area relationships
        - Real extinction dynamics are more complex and species-specific
        - Local factors and conservation efforts can influence outcomes
        """)