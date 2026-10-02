import streamlit as st
import folium
from streamlit_folium import folium_static

def page0_content():
    # Introduction to Biomes
    st.title("Explore Earth's Biomes")
    st.write("Select a biome from the sidebar to learn more about it!")

    # Biomes with detailed descriptions, image paths, locations, and types
    biomes = {
        "Tundra": {
            "desc": [
                "Extremely cold temperatures, with average winter temperatures of -30°C",
                "Permafrost (permanently frozen subsoil)",
                "Short growing season (50-60 days)",
                "Low biodiversity but specialized species like caribou, muskoxen, arctic fox, and polar bears",
                "Small plants like lichens, mosses, and dwarf shrubs that can withstand harsh conditions"
            ],
            "image": "./unit4/images/tundra.webp", 
            "location": [65, -150], 
            "type": "terrestrial"
        },
        "Taiga": {
            "desc": [
                "Coniferous forests dominated by spruce, pine, and fir trees",
                "Long, severe winters and short summers",
                "Acidic, nutrient-poor soil due to the accumulation of needles",
                "Wildlife including moose, wolves, bears, and numerous bird species",
                "Covers much of Canada, Alaska, Russia, and Scandinavia",
                "Critical carbon sink that helps regulate global climate"
            ],
            "image": "./unit4/images/taiga.webp", 
            "location": [60, -100], 
            "type": "terrestrial"
        },
        "Temperate Forest": {
            "desc": [
                "Four distinct seasons with moderate temperatures",
                "30-60 inches of annual precipitation evenly distributed throughout the year",
                "Rich biodiversity with deciduous trees like oak, maple, and beech",
                "Well-defined canopy layers supporting diverse animal life",
                "Rich soils that support agriculture when cleared",
                "Significant seasonal variations, with many trees losing leaves in winter"
            ],
            "image": "./unit4/images/temperate_forest.webp", 
            "location": [45.5756, -69.2366], 
            "type": "terrestrial"
        },
        "Grassland": {
            "desc": [
                "Moderate precipitation (20-35 inches annually) - enough to support grass but not forests",
                "Deep, fertile soils rich in nutrients and organic matter",
                "Home to large grazing mammals like bison, zebras, and antelope",
                "Frequent fires that prevent tree establishment",
                "Often converted to agricultural land due to fertile soils",
                "Cover about 25% of Earth's land and are found on every continent except Antarctica"
            ],
            "image": "./unit4/images/grassland.webp", 
            "location": [40, -100], 
            "type": "terrestrial"
        },
        "Desert": {
            "desc": [
                "Extreme temperature variations between day and night",
                "Very low precipitation (less than 10 inches annually)",
                "Specialized plants with adaptations like waxy cuticles, deep roots, and CAM photosynthesis",
                "Animals with adaptations for water conservation and heat regulation",
                "Sparse vegetation coverage with large areas of exposed soil or sand",
                "Cover approximately 30% of Earth's land surface"
            ],
            "image": "./unit4/images/desert.webp", 
            "location": [30, -110], 
            "type": "terrestrial"
        },
        "Rainforest": {
            "desc": [
                "Receive at least 80 inches of rain annually with high humidity",
                "Home to over 50% of the world's plant and animal species",
                "Complex structure with multiple canopy layers",
                "Rapid nutrient cycling with most nutrients stored in living plants",
                "Poor soil quality despite lush vegetation",
                "Provide crucial ecosystem services including oxygen production and carbon sequestration"
            ],
            "image": "./unit4/images/rainforest.webp", 
            "location": [-3.1625, -71.1939], 
            "type": "terrestrial"
        },
        "Lake": {
            "desc": [
                "Standing bodies of freshwater with distinct ecological zones",
                "Littoral zone (shallow water near shore with rooted plants)",
                "Limnetic zone (open, sunlit water away from shore)",
                "Profundal zone (deep water where light doesn't penetrate)",
                "Benthic zone (lake bottom)",
                "Support diverse communities of plankton, fish, amphibians, and invertebrates"
            ],
            "image": "./unit4/images/lake.webp", 
            "location": [39.0960, -120.0286], 
            "type": "aquatic"
        },
        "River": {
            "desc": [
                "Flowing freshwater ecosystems that change from source to mouth",
                "Headwaters have cold, clear, fast-flowing water with high oxygen content",
                "Middle reaches have wider channels, more nutrients, and diverse habitats",
                "Lower reaches have slower flow, more sediment, and floodplains",
                "Create important riparian zones that support high biodiversity",
                "Serve as migration corridors for many fish species"
            ],
            "image": "./unit4/images/river.webp", 
            "location": [35.5233, -90.0071], 
            "type": "aquatic"
        },
        "Estuary": {
            "desc": [
                "Transitional zones where freshwater rivers meet the ocean",
                "Mixing of fresh and salt water creates brackish conditions",
                "Tidal influences create constantly changing conditions",
                "Extremely productive ecosystems serving as nurseries for many marine species",
                "High nutrient levels support abundant phytoplankton",
                "Critical habitats include salt marshes, mudflats, and mangrove forests"
            ],
            "image": "./unit4/images/estuary.webp", 
            "location": [29.669, -89.8629], 
            "type": "aquatic"
        },
        "Intertidal": {
            "desc": [
                "Exist between high and low tide marks on shorelines",
                "Organisms face extreme conditions with alternating exposure to air and water",
                "Distinct zonation patterns based on tolerance to desiccation",
                "Specialized adaptations for attachment, water retention, and temperature regulation",
                "High biodiversity including algae, barnacles, mussels, sea stars, and crabs",
                "Serve as feeding grounds for many bird species"
            ],
            "image": "./unit4/images/intertidal.webp", 
            "location": [47.9479, -124.6656], 
            "type": "aquatic"
        },
        "Coral Reef": {
            "desc": [
                "Underwater ecosystems built by colonies of tiny animals called coral polyps",
                "Occupy less than 1% of the ocean floor but support 25% of all marine species",
                "Require clear, warm, shallow water with temperatures between 23-29°C",
                "Form through symbiosis between coral polyps and photosynthetic algae",
                "Major reef types include fringing reefs, barrier reefs, and atolls",
                "Provide coastal protection, fisheries, and tourism income"
            ],
            "image": "./unit4/images/coral_reef.webp", 
            "location": [25.4916, -80.1511], 
            "type": "aquatic"
        },
        "Deep Ocean": {
            "desc": [
                "Begins below 200 meters and contains several distinct zones",
                "Mesopelagic (twilight zone): 200-1000m, dim light, many bioluminescent organisms",
                "Bathypelagic (midnight zone): 1000-4000m, complete darkness, cold, high pressure",
                "Abyssopelagic (abyssal zone): 4000-6000m, near freezing temperatures",
                "Hadopelagic (trench zone): 6000m+, extreme pressure (up to 1,100 atmospheres)",
                "Covers over 65% of Earth's surface but less than 20% has been explored"
            ],
            "image": "./unit4/images/deep_ocean.webp", 
            "location": [-30, -100], 
            "type": "aquatic"
        }
    }

    # Initialize session state for selected biome
    if 'selected_biome' not in st.session_state:
        st.session_state.selected_biome = "Tundra"  # Default selection

    # Sidebar biome selection
    st.sidebar.title("Biome Selection")
    biome_selection = st.sidebar.selectbox(
        "Choose a biome", list(biomes.keys()), 
        index=list(biomes.keys()).index(st.session_state.selected_biome)
    )
    
    # Update selected biome based on sidebar selection
    st.session_state.selected_biome = biome_selection
    
    # Get the selected biome's location for map centering
    selected_location = biomes[st.session_state.selected_biome]["location"]
    
    # Create the interactive map with folium - centered on the selected biome
    m = folium.Map(location=selected_location, zoom_start=4)
    
    # Add markers for each biome
    for biome_name, data in biomes.items():
        icon_color = "blue" if data["type"] == "aquatic" else "green"
        
        # Add a special icon style for the selected biome
        if biome_name == st.session_state.selected_biome:
            folium.Marker(
                location=data["location"],
                popup=f"<b>{biome_name}</b>",
                tooltip=biome_name,
                icon=folium.Icon(color=icon_color, icon="star")
            ).add_to(m)
        else:
            folium.Marker(
                location=data["location"],
                popup=f"<b>{biome_name}</b>",
                tooltip=biome_name,
                icon=folium.Icon(color=icon_color)
            ).add_to(m)

    # Add legend to map
    legend_html = '''
    <div style="position: fixed; 
                bottom: 50px; left: 50px; width: 150px; height: 90px; 
                border:2px solid grey; z-index:9999; font-size:14px;
                background-color:white; padding: 10px;
                border-radius: 5px;">
      <p style="margin-bottom: 5px;"><strong>Biome Types</strong></p>
      <div style="display: flex; align-items: center; margin-bottom: 5px;">
        <div style="background-color: green; width: 15px; height: 15px; margin-right: 5px;"></div>
        <span>Terrestrial</span>
      </div>
      <div style="display: flex; align-items: center;">
        <div style="background-color: blue; width: 15px; height: 15px; margin-right: 5px;"></div>
        <span>Aquatic</span>
      </div>
    </div>
    '''
    m.get_root().html.add_child(folium.Element(legend_html))
    
    # Display the map
    folium_static(m, width=700, height=500)
    
    # Display selected biome information
    selected_biome = st.session_state.selected_biome
    if selected_biome:
        biome_data = biomes[selected_biome]
        st.header(f"{selected_biome} Biome")
        
        # Two-column layout for image and description
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.image(biome_data["image"], use_column_width=True)
            st.caption(f"Biome Type: {biome_data['type'].capitalize()}")
        
        with col2:
            st.subheader("Key Characteristics:")
            # Format the description as bullet points
            for bullet in biome_data["desc"]:
                st.markdown(f"• {bullet}")
            
        # Display biome-specific interesting facts
        st.subheader("Did You Know?")
        
        if selected_biome == "Tundra":
            st.info("The tundra is the coldest of all biomes, with extremely low temperatures, little precipitation, poor nutrients, and short growing seasons. The average winter temperature is -34°C (-30°F), but summer temperatures range from 3-12°C (37-54°F), which enables this biome to sustain life.")
        elif selected_biome == "Taiga":
            st.info("The taiga, also known as boreal forest, has low primary productivity compared to temperate and tropical forests. However, its aboveground biomass is high because the slow-growing tree species are long-lived and accumulate standing biomass over time.")
        elif selected_biome == "Temperate Forest":
            st.info("Temperate forests have mild, frost-free winters and high precipitation (more than 150 cm) evenly distributed throughout the year. Though only scattered remnants of original temperate forests remain in many regions.")
        elif selected_biome == "Grassland":
            st.info("Grasslands grade into deciduous forest biomes on their wetter margins and deserts on their drier margins. The borders between grasslands and other biomes are dynamic and shift according to precipitation, disturbance, fire, and drought.")
        elif selected_biome == "Desert":
            st.info("Deserts are dry areas where rainfall is less than 50 centimeters (20 inches) per year. They cover around 20 percent of Earth's surface and can be either cold or hot, although most are found in subtropical areas.")
        elif selected_biome == "Rainforest":
            st.info("In tropical rainforests, cloud cover is visible above much of the area due to high humidity and evaporation, while desert regions often have clear skies due to descending air masses, as visible in aerial photographs of Earth.")
        elif selected_biome == "Lake":
            st.info("Lakes have distinct zones including the littoral zone (shallow water with rooted plants), limnetic zone (open, sunlit water), profundal zone (deep water with no light), and benthic zone (lake bottom).")
        elif selected_biome == "River":
            st.info("When a river reaches an ocean or large lake, the water typically slows dramatically and any silt in the water settles. Rivers with high silt content and minimal currents build deltas, while those with low silt or high ocean currents create estuaries.")
        elif selected_biome == "Estuary":
            st.info("Estuaries are biomes where fresh water meets the ocean, creating brackish water. They provide protected areas where young offspring of crustaceans, mollusks, and fish begin their lives.")
        elif selected_biome == "Intertidal":
            st.info("The intertidal zone varies by shore type. On sandy shores, waves keep mud and sand constantly moving, so few algae and plants can establish themselves, while the fauna includes worms, clams, predatory crustaceans, crabs, and shorebirds.")
        elif selected_biome == "Coral Reef":
            st.info("Coral reefs are incredibly diverse, hosting over a thousand species of fish. Currently, they are in danger due to human-caused climate change, which has led to the ocean growing hotter and more acidic.")
        elif selected_biome == "Deep Ocean":
            st.info("To give perspective on the ocean's depth, the average depth is 4,267 meters. The deepest part, the Mariana Trench, reaches nearly 11,000 meters below sea level, making it the deepest known point on Earth.")
