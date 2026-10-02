import streamlit as st

def page0_content():
    # Introduction to Extinction
    st.header("Introduction to Extinction")

    st.markdown("""
    Extinction is the complete disappearance of a species from Earth. It is a natural part of life, as species evolve, change, and sometimes die out. However, human activity has accelerated the rate of extinctions, and many species are disappearing at an alarming rate due to habitat destruction, climate change, pollution, and overexploitation.
    
    Extinction can occur at various scales, and it is important to understand the different categories of extinction in order to approach conservation efforts effectively.
    """)

    # Definitions of different types of extinction
    st.subheader("Types of Extinction")

    st.markdown("""
    **Extinct**:  
    A species is considered extinct when no individuals of that species are alive anywhere on Earth. The last individual has died, and the species no longer exists.

    **Extinct in the Wild**:  
    A species is categorized as extinct in the wild when the only surviving individuals exist in captivity or cultivation, with no viable populations in their natural habitats.

    **Locally Extinct (Extirpated)**:  
    A species is said to be locally extinct or extirpated when it is no longer found in an area it once inhabited, but can still be found elsewhere in the world.

    **Functionally Extinct**:  
    A species is considered functionally extinct when only a few individuals remain, and these are no longer able to reproduce or fulfill their ecological role within their environment. The species might still exist, but it is essentially lost to its ecosystem.
    """)

    # Discussion Questions
    st.subheader("Discussion Questions")

    st.markdown("""
    1. What are the main drivers of extinction in today's world? How do human activities contribute to these drivers?
    2. Why is it important to understand the different categories of extinction? How do these categories affect our conservation strategies?
    3. What do you think can be done to prevent more species from becoming functionally extinct or extinct in the wild?
    4. How do the consequences of local extinctions impact ecosystems at large? Can you think of an example where the loss of a species in a specific region had cascading effects on the ecosystem?
    5. What roles do zoos, botanical gardens, and seed banks play in preventing extinction? Do you think these efforts are enough to prevent species loss on a large scale?
    """)

