import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def page1_content():

    # Interactive Activity
    st.header("Explore Valuation Methods")
    st.write("Use the sliders and options below to explore different methods used in environmental economics to value species:")

    valuation_method = st.selectbox(
        "Select a Valuation Method:",
        ["Direct Use Value", "Indirect Use Value", "Amenity Value", "Option Value", "Existence Value"]
    )

    if valuation_method == "Direct Use Value":
        st.write("Direct Use Value represents the tangible benefits people obtain directly from species, such as food, medicine, or recreational activities.")
    elif valuation_method == "Indirect Use Value":
        st.write("Indirect Use Value refers to the benefits species provide through ecosystem services, like water purification, climate regulation, and pollination.")
    elif valuation_method == "Amenity Value":
        st.write("Amenity Value is the value of recreational services in nature (e.g., **ecotourism**)")
    elif valuation_method == "Option Value":
        st.write("Option Value is the potential future benefits from species that may not be currently utilized, preserving the option for future use.")
    else:
        st.write("Existence Value is the intrinsic value of knowing that a species or ecosystem exists, regardless of any direct or indirect use.")

    # Case Study or Example
    st.subheader("Case Study: Valuing Pollinators")
    st.write("""
    Consider the example of bees as pollinators. They are essential for agriculture, affecting the production of fruits and vegetables.
    How would you value their contribution to the ecosystem and economy?
    """)
    pollinator_value = st.slider("Estimated Value of Pollinators (in billions of USD):", 0, 100, 10)

    st.write(f"You estimated the value of pollinators at ${pollinator_value} billion USD.")

    # Button to Reveal Actual Value
    if st.button("Reveal Actual Value"):
        st.write("The actual estimated value of pollinators is **$34 billion USD**.")
        st.write("Citation: Alex Jordan, Harland M. Patch, Christina M. Grozinger, and Vikas Khanna (2021),"
                "Economic dependence and vulnerability of the United States agricultural sector on insect-mediated pollination service, "
                "_Environmental Science & Technology_, 2021, **55** (4), 2243-2253, "
                "[DOI: 10.1021/acs.est.0c04786](https://doi.org/10.1021/acs.est.0c04786).")
        st.image("https://pubs.acs.org/cms/10.1021/acs.est.0c04786/asset/images/medium/es0c04786_0006.gif")

        st.write("")
        st.write("**Patterns of Bee Pollinators in the United States**")
        # HTML and CSS for dynamic resizing and centering
        html_code = """
        <div style="display: flex; justify-content: left; width: 100%; margin-bottom: 20px;">
            <div style="width: 75%;">
                <img src="https://www.pnas.org/cms/10.1073/pnas.1218503110/asset/3b01900a-1dea-41c4-9539-f783733c1bf9/assets/graphic/pnas.1218503110fig01.jpeg" style="width: 100%;">
            </div>
        </div>
        """
        
        # Render the HTML
        st.markdown(html_code, unsafe_allow_html=True)
        
        st.write("""
                Citation: Bartomeus, I., Ascher, J. S., Gibbs, J., Danforth, B. N., Wagner, D. L., Hedtke, S. M., & Winfree, R. (2013). 
                Historical changes in northeastern US bee pollinators related to shared ecological traits. 
                _Proceedings of the National Academy of Sciences_, **110** (12), 4656-4660.
                """)

        
        st.write("")
        # Read the CSV file from the URL
        st.write("**United States Blueberry Production**")
        url = "https://raw.githubusercontent.com/lundquist-ecology-lab/conservation_biology/main/data/blueberrystats.csv"
        data = pd.read_csv(url, header=None)
        
        # Extract the years from the first row
        years = data.iloc[0].dropna().astype(int)

        # Extract the numerical data, starting from the second row
        numeric_data = data.iloc[1:]

        # Ensure that the numeric data columns match the length of the years
        numeric_data = numeric_data.loc[:, :len(years)-1]

        # Calculate the mean and standard error, ignoring missing values
        means = numeric_data.apply(pd.to_numeric, errors='coerce').mean()
        se = numeric_data.apply(pd.to_numeric, errors='coerce').sem()
        
        # Plotting the data
        plt.figure(figsize=(10, 6))
        plt.errorbar(years, means, yerr=se, fmt='o-', ecolor='red', capsize=5)
        plt.xlabel('Year')
        plt.ylabel('Production (lbs/acre)')
        plt.title('Average Blueberry Production in the US (1980-2012)')
        plt.legend()
        st.pyplot(plt)

    # Discussion and Reflection
    st.subheader("Discussion questions")
    st.write("1) Why do you think species like bees are valuable? What factors influence their value?")
    st.write("2) What patterns do you see in the graph of blueberry (a bee pollenated fruit) production in the US?")
    st.write("""
            3) Based on the patterns pollinator dependence and bee decline, would you expect the pattern of blueberry production that we see?
            How is the US able to continue to produce blueberries despite the decline in native bees?
            """)

    # Reveal answer
    if st.button("Reveal Answer"):
        st.write("European honey bees are being shipped around the US to provide pollinator service.")
        st.image("https://www.frontiersin.org/files/Articles/850600/fevo-10-850600-HTML-r1/image_m/fevo-10-850600-g002.jpg")
        st.write("Citation: Marcelino, J., Braese, C., Christmon, K., Evans, J. D., Gilligan, T., Giray, T., ... & Ellis, J. D. (2022). The movement of Western honey bees (Apis mellifera L.) among US States and territories: History, benefits, risks, and mitigation strategies. _Frontiers in Ecology and Evolution_, **10**, 850600.")

        # HTML and CSS for dynamic resizing and centering
        html_code = """
        <div style="display: flex; justify-content: left; width: 100%; margin-bottom: 20px;">
            <div style="width: 50%;">
                <img src="https://modernfarmer.com/wp-content/uploads/2023/08/shutterstock_205580095-768x686.jpg" style="width: 100%;">
            </div>
        </div>
        """
        
        # Render the HTML
        st.markdown(html_code, unsafe_allow_html=True)
        st.write("Source: [Modern Farmer](https://modernfarmer.com/2023/08/six-months-on-the-road-inside-the-world-of-migratory-beekeeping/)")
        
        st.subheader("Final question")
        st.write("What might be the negative implications of migratory beekeeping, particularly in relation to environmental impacts?")