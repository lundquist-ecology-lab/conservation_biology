import streamlit as st

def page0_content():
    import streamlit as st

    # Page Title
    st.title("Understanding the Value of Species through Environmental Economics")

    # Introduction
    st.header("Introduction")
    st.write("""
    Environmental economics explores how to balance human activities with environmental preservation.
    One key aspect is understanding the value of species – not just in terms of monetary worth but also in their roles in ecosystems.
    """)

    # Concept Explanation
    st.header("Key Concepts")
    st.write("""
    Species provide various ecosystem services, including:
    - **Provisioning services**: Products like food, fresh water, and medicinal resources.
    - **Regulating services**: Climate regulation, water purification, and pest control.
    - **Cultural services**: Recreational, spiritual, and aesthetic benefits.
    - **Supporting services**: Nutrient cycling, soil formation, and pollination.
    """)

    # Interactive Activity
    st.header("Explore Valuation Methods")
    st.write("Use the sliders and options below to explore different methods used in environmental economics to value species:")

    valuation_method = st.selectbox(
        "Select a Valuation Method:",
        ["Contingent Valuation", "Hedonic Pricing", "Cost-Benefit Analysis"]
    )

    if valuation_method == "Contingent Valuation":
        st.write("Contingent Valuation involves surveys to understand people's willingness to pay for conserving species.")
    elif valuation_method == "Hedonic Pricing":
        st.write("Hedonic Pricing assesses the value of species based on their influence on market prices, such as real estate.")
    else:
        st.write("Cost-Benefit Analysis compares the costs of conservation with the benefits derived from preserving species.")

    # Case Study or Example
    st.header("Case Study: Valuing Pollinators")
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
                "Economic dependence and vulnerability of united states agricultural sector on insect-mediated pollination service, "
                "_Environmental Science & Technology_, 2021, **55** (4), 2243-2253, "
                "[DOI: 10.1021/acs.est.0c04786](https://doi.org/10.1021/acs.est.0c04786).")
        st.image("https://pubs.acs.org/cms/10.1021/acs.est.0c04786/asset/images/medium/es0c04786_0006.gif")
    

    st.subheader("Patterns of bee pollinators in United States")
    st.image("https://www.pnas.org/cms/10.1073/pnas.1218503110/asset/3b01900a-1dea-41c4-9539-f783733c1bf9/assets/graphic/pnas.1218503110fig01.jpeg")
    st.write("""
            Citation: Bartomeus, I., Ascher, J. S., Gibbs, J., Danforth, B. N., Wagner, D. L., Hedtke, S. M., & Winfree, R. (2013). 
            Historical changes in northeastern US bee pollinators related to shared ecological traits. 
            _Proceedings of the National Academy of Sciences_, **110** (12), 4656-4660.
            """)
    
    # Discussion and Reflection
    st.subheader("Discussion questions")
    st.write("Why do you think species like bees are valuable? What factors influence their value?")
    st.write("Native pollinators are on the decline, however ")
    st.wrtie("What patterns do you see in ")

    # Conclusion
    st.header("Conclusion")
    st.write("""
    Understanding the value of species helps in making informed decisions that balance economic growth with conservation efforts.
    Every species plays a unique role, and quantifying their value can support sustainable development.
    """)
