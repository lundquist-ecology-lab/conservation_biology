import streamlit as st
from streamlit_ace import st_ace
import pandas as pd
import pygbif
from pygbif import occurrences as occ
from pygbif import species
import altair as alt
import us
import sys
from io import StringIO
import contextlib
import requests

# Function to capture print output
@contextlib.contextmanager
def capture_output():
    new_out = StringIO()
    old_out = sys.stdout
    try:
        sys.stdout = new_out
        yield sys.stdout
    finally:
        sys.stdout = old_out

def run_user_code(code_str, provided_globals):
    """Execute user code and return output and any created variables"""
    local_vars = {}
    output = ""
    
    # Capture print outputs and execute code
    with capture_output() as out:
        try:
            exec(code_str, provided_globals, local_vars)
            output = out.getvalue()
        except Exception as e:
            output = f"Error: {str(e)}"
    
    return output, local_vars

def search_inaturalist(query):
    """Search iNaturalist for taxa using their API"""
    url = "https://api.inaturalist.org/v1/taxa"
    params = {
        "q": query,
        "per_page": 10,
        "locale": "en"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()['results']
    except Exception as e:
        st.error(f"Error searching iNaturalist: {str(e)}")
        return []

def format_inaturalist_result(result):
    """Format iNaturalist search result for display"""
    info = []
    if result.get('name'):
        info.append(f"Scientific Name: {result['name']}")
    if result.get('preferred_common_name'):
        info.append(f"Common Name: {result['preferred_common_name']}")
    if result.get('rank'):
        info.append(f"Rank: {result['rank']}")
    if result.get('ancestor_ids'):
        info.append(f"iNat ID: {result['id']}")
    if result.get('observations_count'):
        info.append(f"Observations: {result['observations_count']}")
    return " | ".join(info)

def format_gbif_result(result):
    """Format GBIF search result for display"""
    info = []
    if 'scientificName' in result:
        info.append(f"Scientific Name: {result['scientificName']}")
    if 'canonicalName' in result:
        info.append(f"Canonical Name: {result['canonicalName']}")
    if 'rank' in result:
        info.append(f"Rank: {result['rank']}")
    if 'kingdom' in result:
        info.append(f"Kingdom: {result['kingdom']}")
    if 'family' in result:
        info.append(f"Family: {result['family']}")
    if 'key' in result:
        info.append(f"GBIF Taxon Key: {result['key']}")
    return " | ".join(info)

def page0_content():
    # Set up the Streamlit page
    st.title("Interactive GBIF Data Analysis")

    # Add tutorial tabs
    tab1, tab2, tab3, tab4 = st.tabs(["Tutorial", "Interactive Coding", "Data Analysis Examples", "Taxonomy Search"])

    with tab1:
        st.markdown("""
        ## Learning to Query GBIF Data
        
        This platform will help you learn how to query biodiversity data from GBIF using Python. Here's a basic example to get started:
        
        ```python
        # Example code to get iNaturalist observations for a state
        from pygbif import occurrences as occ
        
        # Query GBIF for California observations in 2023
        response = occ.search(
            institutionCode='iNaturalist',
            stateProvince='California',
            year=2023,
            limit=0
        )
        
        print(f"Number of observations: {response['count']}")
        ```
        
        ### Available Functions
        
        1. `occ.search()` - Main function to query GBIF
        
        Key parameters:
        - `institutionCode`: Use 'iNaturalist' to filter for iNat data
        - `stateProvince`: US state name
        - `year`: Year of observation
        - `limit`: Number of records to return (0 for just count)
        
        ### Analysis Ideas
        
        1. Compare observations between two states
        2. Find trends across multiple years
        3. Filter by specific species or taxonomic groups
        """)

    with tab2:
        st.markdown("## Write and Execute Your Code")
        
        # Default code example
        default_code = """# Example: Compare iNaturalist observations between two states
from pygbif import occurrences as occ

# Get data for California
ca_response = occ.search(
    institutionCode='iNaturalist',
    stateProvince='California',
    year=2023,
    limit=0
)

# Get data for New York
ny_response = occ.search(
    institutionCode='iNaturalist',
    stateProvince='New York',
    year=2023,
    limit=0
)

# Create a comparison DataFrame
import pandas as pd
data = {
    'State': ['California', 'New York'],
    'Observations': [ca_response['count'], ny_response['count']]
}
df = pd.DataFrame(data)

# Display results
print("Observation Counts:")
print(df)"""

        # Create the enhanced code editor using st_ace
        user_code = st_ace(
            value=default_code,
            language="python",
            theme="monokai",
            key="ace_editor",
            height=400,
            font_size=14,
            tab_size=4,
            show_gutter=True,
            show_print_margin=True,
            wrap=False,
            auto_update=True,
            readonly=False,
            min_lines=20
        )
        
        # Create globals dict with necessary imports
        globals_dict = {
            'occ': occ,
            'pd': pd,
            'alt': alt,
            'us': us,
            'st': st
        }
        
        # Execute button
        if st.button("Run Code"):
            st.markdown("### Output:")
            output, local_vars = run_user_code(user_code, globals_dict)
            
            # Display any print output in a code block for better formatting
            if output:
                st.code(output, language="text")
            
            # Display any DataFrames created in the code
            # for var_name, var_value in local_vars.items():
            #     if isinstance(var_value, pd.DataFrame):
            #         st.markdown(f"\nDataFrame '{var_name}':")
            #         st.dataframe(var_value)
                    
            #         # Automatically create visualization if it's a comparison DataFrame
            #         if 'State' in var_value.columns and 'Observations' in var_value.columns:
            #             chart = alt.Chart(var_value).mark_bar().encode(
            #                 x=alt.X('State', sort='-y'),
            #                 y='Observations',
            #                 tooltip=['State', 'Observations']
            #             ).properties(
            #                 title='Observations by State',
            #                 width=600,
            #                 height=400
            #             )
            #             st.altair_chart(chart, use_container_width=True)

    with tab3:
        st.markdown("""
        ## Data Analysis Examples
        
        Here are complete examples for creating different types of visualizations with your GBIF data. You can copy these examples and modify them for your needs.
        
        ### Bar Chart Example - Compare States
        ```python
        # Example comparing observations between states
        from pygbif import occurrences as occ
        import pandas as pd
        import altair as alt

        # Get data for multiple states
        states = ['California', 'New York', 'Texas', 'Florida']
        data = []

        for state in states:
            response = occ.search(
                institutionCode='iNaturalist',
                stateProvince=state,
                year=2023,
                limit=0
            )
            data.append({
                'State': state,
                'Observations': response['count']
            })

        # Create DataFrame
        df = pd.DataFrame(data)

        # Create bar chart
        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X('State', sort='-y'),  # Sort bars by height
            y='Observations',
            color='State',
            tooltip=['State', 'Observations']
        ).properties(
            title='GBIF Observations by State (2023)',
            width=600,
            height=400
        )

        st.altair_chart(chart, use_container_width=True)
        ```
                
        ### Time Series Example - Multiple Years
        ```python
        # Example comparing observations across years
        from pygbif import occurrences as occ
        import pandas as pd
        import altair as alt

        # Set up parameters
        states = ['California', 'New York']
        years = list(range(2019, 2024))  # Last 5 years
        data = []

        # Collect data
        for state in states:
            for year in years:
                response = occ.search(
                    institutionCode='iNaturalist',
                    stateProvince=state,
                    year=year,
                    limit=0
                )
                data.append({
                    'State': state,
                    'Year': str(year),  # Convert year to string
                    'Observations': response['count']
                })

        # Create DataFrame
        df = pd.DataFrame(data)

        # Create line chart
        chart = alt.Chart(df).mark_line(point=True).encode(
            x=alt.X('Year:N'),  # Use :N for nominal (categorical) instead of :Q for quantitative
            y='Observations:Q',
            color='State:N',
            tooltip=['State', 'Year', 'Observations']
        ).properties(
            title='GBIF Observations Over Time',
            width=600,
            height=400
        )

        st.altair_chart(chart, use_container_width=True)

        # Display the data
        print("Observations by State and Year:")
        print(df.pivot(index='Year', columns='State', values='Observations'))
        ```
                
        ### Interactive Features Example
        ```python
        # Example with interactive selection
        from pygbif import occurrences as occ
        import pandas as pd
        import altair as alt

        # Get data for multiple states
        states = ['California', 'New York', 'Texas', 'Florida', 'Washington']
        data = []

        for state in states:
            response = occ.search(
                institutionCode='iNaturalist',
                stateProvince=state,
                year=2023,
                limit=0
            )
            data.append({
                'State': state,
                'Observations': response['count']
            })

        # Create DataFrame
        df = pd.DataFrame(data)

        # Create interactive chart
        selection = alt.selection_point(fields=['State'], bind='legend')

        chart = alt.Chart(df).mark_bar().encode(
            x='State',
            y='Observations',
            color='State',
            opacity=alt.condition(selection, alt.value(1), alt.value(0.2)),
            tooltip=['State', 'Observations']
        ).properties(
            title='Interactive GBIF Observations by State',
            width=600,
            height=400
        ).add_params(selection)

        st.altair_chart(chart, use_container_width=True)
        ```

        Each of these examples is complete and ready to use. Just copy the code into the Interactive Coding tab and run it. You can modify the states, years, and other parameters to suit your needs.

        ### Tips for Creating Visualizations:
        1. Always include tooltips for better interactivity
        2. Use appropriate chart types for your data:
        - Bar charts for comparing categories
        - Line charts for time series
        - Area charts for showing proportions over time
        3. Add proper titles and labels
        4. Consider using interactive features for better exploration
        5. Include summary statistics when relevant
        """)

    with tab4:
        st.markdown("""
        ## Taxonomy Search Tool
        
        Use this tool to search for species, families, and other taxonomic groups. The results will provide you with the correct taxonomic keys and names to use in your GBIF queries.
        """)

        # Create search interface
        search_col1, search_col2, search_col3 = st.columns([2, 1, 1])
        
        with search_col1:
            search_term = st.text_input("Enter species name:", 
                                      placeholder="e.g., Monarch butterfly, Danaus plexippus")
        
        with search_col2:
            search_type = st.selectbox("Search type:", 
                                     ["Any Type", "Family"],
                                     index=0)
        
        with search_col3:
            database = st.selectbox("Database:", 
                                  ["GBIF", "iNaturalist"],
                                  index=0)

        if st.button("Search"):
            if search_term:
                with st.spinner(f"Searching {database}..."):
                    try:
                        if database == "GBIF":
                            # GBIF search
                            if search_type == "Family":
                                results = species.name_suggest(q=search_term, rank="FAMILY")
                            else:
                                results = species.name_suggest(q=search_term)
                            
                            if results:
                                st.markdown("### Search Results")
                                st.markdown("Click the copy button to get the formatted code for your query.")
                                
                                for idx, result in enumerate(results[:10]):
                                    display_name = result.get('scientificName', 'Unknown')
                                    
                                    with st.expander(f"Result {idx + 1}: {display_name}"):
                                        st.markdown(format_gbif_result(result))
                                        
                                        taxon_key = result.get('key', '')
                                        scientific_name = result.get('scientificName', '')
                                        family = result.get('family', '')
                                        
                                        st.markdown("#### Query Examples")
                                        
                                        if taxon_key:
                                            st.code(f"""# Search by taxon key
response = occ.search(
    taxonKey={taxon_key},
    limit=10
)""", language="python")
                                        
                                        if scientific_name:
                                            st.code(f"""# Search by scientific name
response = occ.search(
    scientificName="{scientific_name}",
    limit=10
)""", language="python")
                                        
                                        if family:
                                            st.code(f"""# Search by family
response = occ.search(
    family="{family}",
    limit=10
)""", language="python")
                                
                        else:  # iNaturalist search
                            results = search_inaturalist(search_term)
                            
                            if results:
                                st.markdown("### Search Results")
                                st.markdown("Click the copy button to get the formatted code for your query.")
                                
                                for idx, result in enumerate(results):
                                    display_name = result.get('name', 'Unknown')
                                    if result.get('preferred_common_name'):
                                        display_name += f" ({result['preferred_common_name']})"
                                    
                                    with st.expander(f"Result {idx + 1}: {display_name}"):
                                        st.markdown(format_inaturalist_result(result))
                                        
                                        scientific_name = result.get('name', '')
                                        
                                        if scientific_name:
                                            st.markdown("#### Query Examples")
                                            st.code(f"""# Search by scientific name
response = occ.search(
    scientificName="{scientific_name}",
    limit=10
)""", language="python")
                                            
                                            st.code(f"""# Search iNaturalist observations
response = occ.search(
    scientificName="{scientific_name}",
    institutionCode="iNaturalist",
    limit=10
)""", language="python")
                            
                            else:
                                st.warning("No results found. Try modifying your search terms.")
                    
                    except Exception as e:
                        st.error(f"An error occurred while searching: {str(e)}")
            else:
                st.warning("Please enter a search term.")

        # Add helpful usage examples
        with st.expander("See Example Searches"):
            st.markdown("""
            Try these example searches:
            
            - Scientific names:
              - "Danaus plexippus" (Monarch butterfly)
              - "Panthera leo" (Lion)
              - "Quercus alba" (White oak)
            
            - Common names:
              - "Monarch butterfly"
              - "American robin"
              - "White oak"
            
            - Families:
              - "Felidae" (Cats)
              - "Nymphalidae" (Brush-footed butterflies)
              - "Fagaceae" (Beech family)
            """)
        
        # Add explanation of taxonomic ranks
        with st.expander("Understanding Taxonomic Ranks"):
            st.markdown("""
            GBIF uses standard taxonomic ranks for classification:
            
            1. Kingdom (e.g., Animalia, Plantae)
            2. Phylum (e.g., Chordata, Arthropoda)
            3. Class (e.g., Mammalia, Insecta)
            4. Order (e.g., Carnivora, Lepidoptera)
            5. Family (e.g., Felidae, Nymphalidae)
            6. Genus (e.g., Panthera, Danaus)
            7. Species (e.g., Panthera leo, Danaus plexippus)
            
            When searching, you can use any of these ranks to find the appropriate taxonomic keys for your queries.
            """)

    # Add helpful links and resources
    st.markdown("""
    ---
    ### Additional Resources
    - [GBIF API Documentation](https://www.gbif.org/developer/summary)
    - [pygbif Documentation](https://pygbif.readthedocs.io/)
    - [Altair Visualization Documentation](https://altair-viz.github.io/)
    - [Pandas Documentation](https://pandas.pydata.org/docs/)
    - [iNaturalist API Documentation](https://api.inaturalist.org/v1/docs/)
    """)

