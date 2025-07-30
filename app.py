import streamlit as st
import pandas as pd

# Read the Excel file
df = pd.read_excel('SIIB.xlsx')

# Display the data
st.title("SIIB Data Preview")
st.write(df)
