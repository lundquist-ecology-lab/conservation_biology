import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from io import BytesIO
from PIL import Image
import time

def simulate_invasion(grid_size, time_steps, initial_points, spread_rate, barriers_map):
    invasion = np.zeros((time_steps, grid_size, grid_size))
    np.random.seed(42)
    count = 0
    while count < initial_points:
        x, y = np.random.randint(0, grid_size, 2)
        if invasion[0, x, y] == 0:
            invasion[0, x, y] = 100
            count += 1

    for t in range(1, time_steps):
        invasion[t] = invasion[t - 1].copy()
        for i in range(grid_size):
            for j in range(grid_size):
                if invasion[t - 1, i, j] > 0:
                    growth = spread_rate * invasion[t - 1, i, j] * (1 - invasion[t - 1, i, j] / 1000)
                    invasion[t, i, j] += growth
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            ni, nj = i + di, j + dj
                            if 0 <= ni < grid_size and 0 <= nj < grid_size and not barriers_map[ni, nj]:
                                invasion[t, ni, nj] += 0.05 * invasion[t - 1, i, j]
        invasion[t] = np.clip(invasion[t], 0, 1000)
    return invasion

def generate_connected_barriers(grid_size, barrier_count):
    barriers_map = np.zeros((grid_size, grid_size), dtype=bool)
    for _ in range(barrier_count):
        x, y = np.random.randint(0, grid_size, 2)
        length = np.random.randint(10, 25)
        directions = np.array([(1, 0), (0, 1), (1, 1), (-1, 1)])
        direction = directions[np.random.choice(len(directions))]
        for _ in range(length):
            if 0 <= x < grid_size and 0 <= y < grid_size:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < grid_size and 0 <= ny < grid_size:
                            barriers_map[nx, ny] = True
            x += direction[0] + np.random.choice([-1, 0, 1])
            y += direction[1] + np.random.choice([-1, 0, 1])
    return barriers_map

def page6_content():
    colors = [(0.0, 0.0, 0.0, 0.0), (0.0, 0.5, 0.0, 0.5), (1.0, 1.0, 0.0, 0.8), (1.0, 0.0, 0.0, 1.0)]
    invasion_cmap = LinearSegmentedColormap.from_list("invasion_cmap", colors, N=100)

    background_tab, sim_tab, discuss_tab = st.tabs(["📚 Background", "🧪 Simulation", "🧠 Discussion Questions"])

    with background_tab:
        st.title("Understanding Invasive Species")
        st.markdown("""
        Invasive species are organisms that are introduced to an environment where they are not native and cause harm to the local ecosystem, economy, or human health.
        
        **Why are invasive species a concern in conservation biology?**
        - They can outcompete native species for resources.
        - They may lack natural predators in their new environment.
        - They can disrupt ecosystem functions and alter habitats.
        - Management is often expensive and difficult once an invasion is underway.
        
        **Examples of Invasive Species:**
        - **Zebra Mussels** in North America’s Great Lakes.
        - **Cane Toads** in Australia.
        - **Emerald Ash Borer** in North America.
        - **Kudzu Vine** in the southeastern U.S.
        
        Understanding how invasive species spread can help scientists and managers anticipate future impacts and plan effective control strategies.
        """)

    with sim_tab:
        st.title('Invasive Species Spread Simulation')
        st.write("""
        This simulation demonstrates how invasive species spread across different landscapes over time.
        Use Step 1 to configure and run the simulation. Then proceed to Step 2 to play the animation.
        """)

        st.header("Step 1: Model Parameters")

        with st.expander("📘 What do the options mean?"):
            st.markdown("""
            - **Spread Rate**: How fast the species grows and spreads locally.
            - **Initial Introduction Points**: Number of separate invasion starting locations.
            - **Natural Barriers**: Creates connected features (rivers, mountains) that prevent spread.
            """)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Species Characteristics")
            spread_rate = st.slider("Spread Rate", 0.1, 2.0, 0.8)
            initial_points = st.slider("Initial Introduction Points", 1, 5, 1)

        with col2:
            st.subheader("Landscape Characteristics")
            barriers = st.slider("Natural Barriers", 0, 100, 20)

        with st.expander("Advanced Settings"):
            grid_size = st.slider("Map Size", 30, 100, 50)
            time_steps = st.slider("Simulation Duration (years)", 5, 50, 20)
            fps = st.slider("Animation Speed (frames/sec)", 1, 10, 5)
            delay = 1.0 / fps

        rerun_button = st.button("Run Simulation")

        if rerun_button:
            np.random.seed(42)
            st.session_state.barriers_map = generate_connected_barriers(grid_size, barrier_count=barriers)
            st.session_state.invasion_results = simulate_invasion(grid_size, time_steps, initial_points, spread_rate, st.session_state.barriers_map)
            st.session_state.pre_rendered_frames = []
            for t in range(time_steps):
                fig, ax = plt.subplots(figsize=(10, 6))
                inv_data = st.session_state.invasion_results[t]
                max_val = max(1, np.max(inv_data))
                norm_data = inv_data / max_val
                ax.imshow(norm_data, cmap=invasion_cmap, vmin=0, vmax=1, origin='lower')
                barrier_y, barrier_x = np.where(st.session_state.barriers_map)
                ax.scatter(barrier_x, barrier_y, color='blue', marker='x', s=10, alpha=0.5, label='Barriers')
                ax.set_title(f'Invasive Species Spread (Year {t+1})')
                ax.set_xlabel('X')
                ax.set_ylabel('Y')
                fig.tight_layout()
                buf = BytesIO()
                fig.savefig(buf, format='png', dpi=100, bbox_inches='tight')
                buf.seek(0)
                st.session_state.pre_rendered_frames.append(Image.open(buf))

        st.header("Step 2: Play Animation")
        play_button = st.button("Play/Pause Animation")

        animation_placeholder = st.empty()
        year_display = st.empty()
        col1, col2 = st.columns(2)
        area_metric = col1.empty()
        front_metric = col2.empty()

        if 'animating' not in st.session_state:
            st.session_state.animating = False

        if play_button:
            st.session_state.animating = not st.session_state.animating

        if 'current_frame' not in st.session_state:
            st.session_state.current_frame = 0

        if 'pre_rendered_frames' in st.session_state and st.session_state.animating:
            total_frames = len(st.session_state.pre_rendered_frames)
            year_idx = st.session_state.current_frame % total_frames  # safe wraparound

            year_num = year_idx + 1
            img = st.session_state.pre_rendered_frames[year_idx]
            animation_placeholder.image(img, use_column_width=True)
            year_display.markdown(f"**Year: {year_num} of {total_frames}**")

            inv_data = st.session_state.invasion_results[year_idx]
            invaded_cells = np.sum(inv_data > 0)
            invasion_percent = (invaded_cells / (grid_size * grid_size)) * 100
            # Expansion front: invaded cells that border at least one uninvaded cell
            invaded = inv_data > 0
            padded = np.pad(invaded, 1, constant_values=True)
            all_neighbors_invaded = (padded[:-2, 1:-1] & padded[2:, 1:-1]
                                     & padded[1:-1, :-2] & padded[1:-1, 2:])
            edge_cells = int(np.sum(invaded & ~all_neighbors_invaded))
            expansion_percent = f"{edge_cells / invaded_cells * 100:.1f}%" if invaded_cells else "0.0%"

            area_metric.metric("Area Invaded", f"{invaded_cells} cells", f"{invasion_percent:.1f}% of landscape")
            front_metric.metric("Expansion Front", f"{edge_cells} cells", f"{expansion_percent} of invaded area")

            st.session_state.current_frame = (year_idx + 1) % total_frames
            time.sleep(delay)
            st.rerun()

    with discuss_tab:
        st.header("Discussion Questions")
        st.markdown("""
        1. **How does the spread rate affect invasion dynamics?**
        2. **What role do natural barriers play in altering invasion routes?**
        3. **What kinds of real-world landscapes might resemble these barriers?**
        4. **How could this type of model inform invasive species management?**
        5. **What are some limitations of this simulation model?**
        """)

if __name__ == "__main__":
    page6_content()

