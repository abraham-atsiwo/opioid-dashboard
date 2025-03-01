
import streamlit as st 
from .state_multiselect import state_multiselect
from .load_data import load_data

# Create a multiselect widget
def display_data_states(states: str, eval_function: callable = None, kwargs: dict = None):
    # Define the range of years
    min_year = 1999
    max_year = 2022

    # Create a range slider with increment of 1
    year_range = st.slider(
        "select a range of years",
        min_value=min_year,  # Minimum value (1999)
        max_value=max_year,  # Maximum value (2022)
        value=(min_year, max_year),  # Default range (1999 to 2022)
        step=1  # Increment by 1
    )
    # Unpack the selected range
    start_year, end_year = year_range

    selected_states = state_multiselect(states=states, key='states-id')
    # Add a checkbox for 'Select All' functionality
    if st.checkbox('Select All'):
        selected_states = states

    st.write('You selected:', selected_states)

    tab_names = list(selected_states)

    # Create tabs dynamically
    tabs = st.tabs(tab_names)  # This creates the tabs and returns a list of tab objects

    # Add content to each tab
    for i, tab in enumerate(tabs):
        # with tab:
        #     st.header(f"sample Data for {tab_names[i]}")
        #     df = load_data(state=tab_names[i], start_year=start_year, end_year=end_year)
        #     st.write(df.head())
        #     st.divider()
        #     st.header(f"{kwargs['title']} {tab_names[i]}")
        #     st.write(eval_function(df=df, state=tab_names[i]))

        with tab:
            try:
                st.header(f"sample data for {tab_names[i]}")
                df = load_data(state=tab_names[i], start_year=start_year, end_year=end_year)
                st.write(df.head())
                st.divider()
                st.header(f"{kwargs['title']} {tab_names[i]}")
                st.write(eval_function(df=df, state=tab_names[i]))
            except:
                st.write(f"Error in Processing {tab_names[i]} Data")
                # st.write(Exception)

  