import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# from pmdarima import auto_arima

from utils.constants import states
from utils.display_data_state import display_data_states


def eval_function(df, state=None):
    # Add a dropdown to select the column

    cols = list(df.columns)
    cols.remove("Year")
    cols.remove("Growth Rate")
    selected = st.selectbox(
        "Select the column to fit the polynomial", cols, index=4, key=state
    )
    # Add a slider to select the degree of the polynomial
    degree = st.slider(
        "Select the degree of the polynomial",
        min_value=1,
        max_value=10,
        value=3,
        key=f"{state}_slider",
    )
    # Fit the polynomial
    x_values = df["Year"]  # Use the 'Year' column as the x-axis
    y_values = df[selected]

    # Compute polynomial coefficients
    coefficients = np.polyfit(x_values, y_values, deg=degree)

    # Create a polynomial function
    with st.spinner("Fitting Parameters."):
        polynomial = np.poly1d(coefficients)

        # Generate fitted values
        fitted_values = polynomial(x_values)

        # Predict values for 2023, 2024, and 2025
        pred = np.array(x_values)[-1]
        future_years = np.array([pred + 1, pred + 2, pred + 3])
        future_values = polynomial(future_years)

        # Create a DataFrame for future predictions
        actual = [np.nan, np.nan, np.nan]

        future_df = pd.DataFrame(
            {"Year": future_years, "Predicted Value": future_values}
        )

        # Plot the original data, fitted polynomial, and future predictions
        st.write("### polynomial fit with future predictions")
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(x_values, y_values, label="Original Data", color="blue")
        ax.plot(
            x_values,
            fitted_values,
            label=f"Polynomial Fit (Degree {degree})",
            color="red",
        )
        ax.scatter(
            future_years,
            future_values,
            label="Future Predictions",
            color="green",
            marker="x",
            s=100,
        )
        ax.set_title(f"polynomial fit (Degree {degree})")
        ax.set_xlabel("Year")
        ax.set_ylabel(selected)
        ax.legend()
        st.pyplot(fig)
        plt.close(fig)  # Close the figure to free up memory

        # Display the polynomial equation using LaTeX
        st.write("### polynomial equation")
        equation = " + ".join(
            [f"{coeff:.2f}x^{i}" for i, coeff in enumerate(coefficients[::-1])]
        )
        st.latex(f"y = {equation}")

        # Display the future predictions in a table
        # Center the heading using HTML and CSS
        st.markdown(
            """
            <h3 style='text-align: center;'>future predictions</h3>
            """,
            unsafe_allow_html=True,
        )

        # Convert the DataFrame to HTML
        df_html = future_df.to_html(index=False)

        # Center the DataFrame using HTML and CSS
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center;">
                {df_html}
            </div>
            """,
            unsafe_allow_html=True,
        )

    return ""

display_data_states(
    eval_function=eval_function, states=states, kwargs={"title": "modeling"}
)
