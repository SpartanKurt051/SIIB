import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# Read the Excel file
df = pd.read_excel('SIIB.xlsx')

# Display the data
st.write(df)


st.markdown("""
    <style>
        .main {
            padding-left: 0rem;
            padding-right: 0rem;
        }
        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
            width: 100vw;
            max-width: 100vw;
        }
         .css-1r6slb3 {
            margin-left: 40px !important;
        }
    </style>
""", unsafe_allow_html=True)

#st.title("Hello world")
# Create two columns for layout (side by side)
col1, col2 = st.columns([1, 1], gap="large")

# Left section: 3 pie charts
with col1:
   pass

# Right section: 3 pie charts
with col2:
   pass
