import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt

from utils.constants import states 
from utils.display_data_state import display_data_states 



def eval_function(df, state):
    # df['first_difference_opd_per100K'] = df['opioid_death_per_100K'].diff()
    cols = list(df.columns)
    cols.remove('Year')
    selected = st.selectbox(label='select column', options=cols, index=5, key=state)
    st.write(selected)


    tabs = st.tabs(["Line Plot", "Boxplot", "ACF", "PACF"])

    with tabs[0]:
        fig = go.Figure()
        # Add a line trace with dots
        fig.add_trace(go.Scatter(
            x=df['Year'],  # X-axis data
            y=df[selected],  # Y-axis data
            mode='lines+markers',  # Display both lines and markers
            name='Value',  # Legend name
            marker=dict(size=10, color='red'),  # Customize markers
            line=dict(color='blue', width=2)  # Customize line
        ))
        # Update layout
        fig.update_layout(
            title= f"line plot of {selected}",
            xaxis_title="Year",
            yaxis_title="Value",
            template="plotly_dark"
        )
        st.plotly_chart(fig)
    
    with tabs[1]:
        fig = px.box(
        df,  # DataFrame
        y=selected,  # Column for y-axis (values)
        title="Boxplot of Values",  # Title of the plot
        labels={selected: selected},  # Axis labels
        points="all"  # Show all data points
        )
        st.plotly_chart(fig)
    
    with tabs[2]:
        fig, ax = plt.subplots(figsize=(10, 6))
        plot_acf(df[selected], ax=ax)  # Plot ACF for 20 lags
        plt.title("Autocorrelation Function (ACF)")
        plt.xlabel("Lags")
        plt.ylabel("Autocorrelation")
        st.pyplot(fig)
        plt.close(fig)

    with tabs[3]:
        fig, ax = plt.subplots(figsize=(10, 6))
        plot_pacf(df[selected], ax=ax)  # Plot ACF for 20 lags
        plt.title("Autocorrelation Function (ACF)")
        plt.xlabel("Lags")
        plt.ylabel("Partial Autocorrelation")
        st.pyplot(fig)
        plt.close(fig)

    return ""


    

display_data_states(states=states, eval_function=eval_function, kwargs={'title': "data visualization"})