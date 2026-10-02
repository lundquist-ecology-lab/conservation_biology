import streamlit as st

def page8_content():
    # Custom CSS for styling - Dark Theme (More Subtle)
    st.markdown("""
    <style>
        .main-header {
            color: #E8E3E3;
            font-size: 32px;
            font-weight: 600;
            margin-bottom: 25px;
            border-bottom: 1px solid rgba(140, 151, 125, 0.5);
            padding-bottom: 8px;
        }
        
        .value-title {
            color: #E8E3E3;
            font-size: 20px;
            font-weight: 500;
            margin-top: 20px;
            margin-bottom: 12px;
            padding-left: 10px;
            border-left: 2px solid rgba(140, 151, 125, 0.7);
        }
        
        .value-container {
            background-color: rgba(66, 66, 66, 0.5);
            border-radius: 8px;
            padding: 18px;
            margin-bottom: 22px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
            transition: all 0.25s ease;
        }
        
        .value-container:hover {
            transform: translateY(-3px);
            box-shadow: 0 3px 6px rgba(0, 0, 0, 0.25);
            background-color: rgba(74, 74, 74, 0.5);
        }
        
        .value-text {
            margin-top: 12px;
            font-size: 15px;
            line-height: 1.5;
            color: rgba(232, 227, 227, 0.9);
        }
        
        .image-container {
            overflow: hidden;
            border-radius: 6px;
            margin-top: 8px;
            border: 1px solid rgba(85, 85, 85, 0.3);
        }
        
        .image-container img {
            transition: transform 0.4s ease;
            width: 100%;
            opacity: 0.95;
        }
        
        .image-container:hover img {
            transform: scale(1.03);
            opacity: 1;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Main header
    st.markdown('<h1 class="main-header">Values of Conservation Biology</h1>', unsafe_allow_html=True)
    
    # Value 1
    st.markdown('<h2 class="value-title">1. Biological diversity has intrinsic value</h2>', unsafe_allow_html=True)
    
    # Image with container for styling
    st.markdown("""
    <div class="image-container">
        <img src="https://images.unsplash.com/photo-1448375240586-882707db888b?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D">
    </div>
    <p class="value-text">
        Biodiversity is valuable in itself, independent of its usefulness to humans. Each species, 
        ecosystem, and genetic variant represents millions of years of evolution and adaptation.
    </p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Value 2
    st.markdown('<h2 class="value-title">2. Extinction of populations and species caused by human impacts should be prevented</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="image-container">
        <img src="https://images.unsplash.com/photo-1468560721961-0c42d2f9dcf9?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D">
    </div>
    <p class="value-text">
        Human activities are causing species to go extinct at rates far exceeding natural background 
        extinction. Conservation biology seeks to understand and mitigate these impacts.
    </p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Value 3
    st.markdown('<h2 class="value-title">3. Species diversity and complexity of communities should be preserved</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="image-container">
        <img src="https://images.unsplash.com/photo-1682695797221-8164ff1fafc9?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D">
    </div>
    <p class="value-text">
        Ecological communities with high diversity tend to be more resilient and productive. 
        Conservation efforts should focus on maintaining the complexity and interconnectedness of natural systems.
    </p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Value 4
    st.markdown('<h2 class="value-title">4. Science has a critical role in understanding ecosystems</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="image-container">
        <img src="https://images.unsplash.com/photo-1518152006812-edab29b069ac?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D">
    </div>
    <p class="value-text">
        Sound conservation policy must be grounded in rigorous scientific research. Understanding the 
        complex dynamics of ecosystems requires ongoing study and monitoring.
    </p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Value 5
    st.markdown('<h2 class="value-title">5. Collaboration between different sectors is important/necessary</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="image-container">
        <img src="https://images.unsplash.com/photo-1552799446-159ba9523315?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D">
    </div>
    <p class="value-text">
        Effective conservation requires cooperation between governments, NGOs, businesses, local communities, 
        and scientists. Complex environmental challenges demand multidisciplinary approaches and diverse perspectives.
    </p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
