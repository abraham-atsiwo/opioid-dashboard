import streamlit as st 

def state_multiselect(states, key, default="Nevada", title = "Select States"):
    return st.multiselect(title, states, default=default)