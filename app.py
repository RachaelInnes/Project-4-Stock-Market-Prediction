import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Create a connection to the PostgreSQL database
@st.cache_data
def load_data():
    engine = create_engine('postgresql+psycopg2://postgres:Arabella08@localhost:5432/Stock_Market_Project')
    query = "SELECT * FROM cleaned_stock_data"
    df = pd.read_sql(query, engine)
    return df

# Load data
df = load_data()

# Streamlit UI
st.title("Stock Market Prediction")
st.write("Here is the cleaned stock data:")
st.dataframe(df)

# Select a stock
stock_options = ['AMZN', 'GOOGL', 'IBM', 'MSFT']  # Add your available stocks
selected_stock = st.selectbox("Select a stock:", stock_options)

# Input for prediction threshold
threshold = st.slider("Select price change threshold (%)", 0.0, 10.0, 1.0)

# Input for investment amount
investment_amount = st.number_input("Enter your investment amount:", min_value=0, step=100)

# Button to make a prediction
if st.button("Make Prediction"):
    # Here you would include the logic to predict if the user should buy/sell
    # This is a placeholder for your prediction logic
    # For demonstration purposes, we'll generate a simple mock prediction
    prediction = "Buy" if threshold > 5 else "Sell"  # Replace with your model's prediction logic

    # Display the result
    st.write(f"The recommendation for {selected_stock} is to: **{prediction}**")
    potential_return = (investment_amount * (1 + threshold / 100)) if prediction == "Buy" else (investment_amount * (1 - threshold / 100))
    st.write(f"Potential return based on threshold: ${potential_return:.2f}")

