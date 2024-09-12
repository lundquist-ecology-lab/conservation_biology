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
pollinator_value = st.slider("Estimated Value of Pollinators (in billions of USD):", 0, 100, 30)

st.write(f"You estimated the value of pollinators at ${pollinator_value} billion USD.")

# Discussion and Reflection
st.header("Your Thoughts")
user_input = st.text_area("Why do you think species like bees are valuable? What factors influence their value?")
if user_input:
    st.write("Your thoughts:", user_input)

# Conclusion
st.header("Conclusion")
st.write("""
Understanding the value of species helps in making informed decisions that balance economic growth with conservation efforts.
Every species plays a unique role, and quantifying their value can support sustainable development.
""")
