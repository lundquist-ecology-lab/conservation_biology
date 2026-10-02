import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.colors import LinearSegmentedColormap
from scipy import ndimage

def page3_content():
    # Title and Introduction
    st.title("Habitat Fragmentation Simulation")
    st.markdown("""
    **Learning Objective:**
    This simulation explores how habitat fragmentation impacts species by dividing a continuous habitat into smaller, isolated patches.
    
    **Habitat Fragmentation:**
    Habitat fragmentation occurs when large habitats are broken into smaller, isolated patches, often due to human activities such as urban development or agriculture. Fragmentation can limit animal movement, reduce biodiversity, and disrupt ecosystems.
    """)

    # User Input for Simulation Parameters
    st.header("Fragmentation Simulation Settings")
    
    grid_size = st.slider("Choose the grid size (number of cells per side):", 5, 50, 20)
    fragmentation_steps = st.slider("Level of fragmentation (number of cuts to the habitat):", 0, grid_size * 2, 0)

    # Create a single contiguous habitat patch with terrain variation
    base_terrain = np.ones((grid_size, grid_size))
    
    # Add terrain variation (slight height/density differences)
    terrain_variation = np.random.normal(0, 0.15, (grid_size, grid_size))
    grid = np.clip(base_terrain + terrain_variation, 0.5, 1.5)
    
    # Apply smoothing for more natural terrain
    grid = ndimage.gaussian_filter(grid, sigma=1.0)

    # Randomly fragment the habitat by removing connections
    for _ in range(fragmentation_steps):
        # Pick a random cell from the grid to "cut"
        row = random.randint(0, grid_size - 1)
        col = random.randint(0, grid_size - 1)
        
        # Create a small patch of fragmentation (not just a single cell)
        patch_size = random.randint(1, 3)
        for i in range(max(0, row - patch_size), min(grid_size, row + patch_size + 1)):
            for j in range(max(0, col - patch_size), min(grid_size, col + patch_size + 1)):
                # Add some randomness to the patch shape
                if random.random() < 0.7:
                    grid[i, j] = 0.0  # Non-habitat area

    # Visualization of Habitat Fragmentation
    st.header("Habitat Fragmentation Visualization")
    
    # Create a custom colormap for the terrain
    colors = [(0.9, 0.9, 0.9), (0.2, 0.6, 0.3), (0.0, 0.4, 0.1)]  # Road/urban, light forest, dense forest
    cmap = LinearSegmentedColormap.from_list("terrain_cmap", colors, N=256)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    im = ax.imshow(grid, cmap=cmap, interpolation="bilinear")
    
    # Remove cell labels and just show the terrain
    plt.title("Fragmented Habitat Visualization")
    plt.xticks([])
    plt.yticks([])
    
    # Add a colorbar to show the terrain density
    cbar = plt.colorbar(im, ax=ax, shrink=0.6)
    cbar.set_label("Habitat Density")
    
    st.pyplot(fig)

    # Display Effect of Fragmentation on Biodiversity
    st.header("Impact of Fragmentation on Species Movement and Biodiversity")
    
    # Calculate connected components to identify isolated habitat patches
    binary_grid = (grid > 0.3).astype(int)  # Threshold for habitat vs non-habitat
    labeled_array, num_patches = ndimage.label(binary_grid)
    
    st.write(f"**Number of isolated habitat patches:** {num_patches}")
    
    if fragmentation_steps > grid_size**2 // 2:
        st.write("""
        **Severe fragmentation:** Species movement between habitat patches is highly restricted. This can lead to a loss of biodiversity, inbreeding, and local extinctions in smaller patches.
        """)
    elif fragmentation_steps > grid_size**2 // 4:
        st.write("""
        **Moderate fragmentation:** Some species are able to move between patches, but the fragmented landscape still restricts migration and gene flow, reducing biodiversity over time.
        """)
    else:
        st.write("""
        **Low fragmentation:** Species can move freely between patches, allowing for gene flow and species migration. However, the habitat is still fragmented, which may limit the range of larger animals or species with specific habitat requirements.
        """)

    # Critical Thinking Section
    st.header("Critical Thinking Questions")

    st.markdown("""
    1. **What are the potential long-term consequences of habitat fragmentation for species that rely on large continuous habitats?**  
       How might their movement, breeding, and survival be affected in a highly fragmented landscape?

    2. **How does the level of isolation between habitat patches affect species diversity?**  
       Consider how gene flow, species migration, and population size are impacted by different levels of isolation.

    3. **What human activities are most responsible for causing habitat fragmentation?**  
       Are there any conservation efforts or policies that can mitigate the effects of fragmentation?

    4. **Can fragmented habitats still support healthy ecosystems?**  
       In what cases might fragmented habitats maintain biodiversity, and when might they lead to declines in species populations?
    """)
