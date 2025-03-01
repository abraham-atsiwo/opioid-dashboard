import streamlit as st

from utils.constants import states 
from utils.display_data_state import display_data_states 


def eval_function(df, state: str = None):
    # st.write(state)
    return df.describe()

display_data_states(states=states, eval_function=eval_function, kwargs={'title': "summary statistics"})