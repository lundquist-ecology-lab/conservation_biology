import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import base64
import os

def page4_content():
    st.title("Genetic Drift, Population Size, and the Extinction Vortex")

    # Introduction
    st.header("Genetic Drift and Population Size")
    st.write("""
    Genetic drift refers to random changes in allele frequencies due to chance events. It has a more significant impact on smaller populations, where even random fluctuations can cause substantial genetic changes, potentially leading to the loss of genetic diversity and increased vulnerability to extinction.
    """)

    st.subheader("Effective Population Size (Ne)")
    st.latex(r'''Ne = \frac{4 \cdot N_m \cdot N_f}{N_m + N_f}''')
    n_males = st.slider('Number of breeding males (Nm)', 1, 500, 50)
    n_females = st.slider('Number of breeding females (Nf)', 1, 500, 50)
    ne = (4 * n_males * n_females) / (n_males + n_females)
    st.write(f"**Calculated Ne:** {ne:.2f}")

    st.subheader("Demographic Stochasticity")
    st.write("""
    Random variation in birth and death rates affects small populations more drastically.
    """)

    pop_size = st.slider("Population Size", 10, 1000, 100, step=10)
    generations = st.slider("Generations", 10, 100, 50, step=10)

    def genetic_drift_two_alleles(pop_size, generations):
        freq_A = [0.5]
        freq_B = [0.5]
        for _ in range(generations):
            if freq_A[-1] in [0, 1]:
                freq_A.append(freq_A[-1])
                freq_B.append(freq_B[-1])
            else:
                next_A = freq_A[-1] + np.random.normal(0, 1 / np.sqrt(pop_size))
                next_A = min(max(next_A, 0), 1)
                freq_A.append(next_A)
                freq_B.append(1 - next_A)
        return freq_A, freq_B

    freq_A, freq_B = genetic_drift_two_alleles(pop_size, generations)
    fig, ax = plt.subplots()
    ax.plot(freq_A, label="Allele A", color='blue')
    ax.plot(freq_B, label="Allele B", color='orange')
    ax.set_xlabel("Generations")
    ax.set_ylabel("Frequency")
    ax.set_title("Genetic Drift Over Generations")
    ax.legend()
    st.pyplot(fig)

    st.subheader("The Extinction Vortex")

    st.write("""
    In the blelow animation, the yellow ball represents a small population in decline. With each loop downward, genetic variation decreases, and extinction risk increases. At the same time, the further down the spiral a population is, the harder it is to reverse.
    """)

    # Display Manim animation if available
    video_path = os.path.join(os.path.dirname(__file__), "extinction_vortex_animation.mp4")

    if os.path.exists(video_path):
        # Convert to base64 for embedding
        with open(video_path, "rb") as f:
            video_bytes = f.read()
            video_b64 = base64.b64encode(video_bytes).decode()

        video_html = f"""
        <video width="100%" autoplay loop muted playsinline>
            <source src="data:video/mp4;base64,{video_b64}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        """

        st.markdown(video_html, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Could not find the animation video.")

