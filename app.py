import streamlit as st

st.title("Hello world")
import pandas as pd

df = pd.read_excel('Case-Role_Engagement_Case.xlsx')
st.write(df)  # Display the dataframe

st.bar_chart(df)  # Simple bar chart (works if your data is numeric)
