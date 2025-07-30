import streamlit as st
import pandas as pd

# Read the Excel file
df = pd.read_excel('SIIB.xlsx')

# Display the data
st.title("SIIB Data Preview")
st.write(df)

import matplotlib.pyplot as plt

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

st.title("Hello world")
# Create two columns for layout (side by side)
col1, col2 = st.columns([1, 1], gap="large")


def dummy_pie_chart(title):
    # Dummy data
    sizes = [30, 30, 40]
    labels = ['A', 'B', 'C']
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax.set_title(title)
    return fig

# Left section: 3 pie charts
with col1:
    st.subheader("Section 1")
    st.pyplot(dummy_pie_chart("Pie Chart 1"))
    st.pyplot(dummy_pie_chart("Pie Chart 2"))
    st.pyplot(dummy_pie_chart("Pie Chart 3"))

# Right section: 3 pie charts
with col2:
    st.subheader("Section 2")
    st.pyplot(dummy_pie_chart("Pie Chart 4"))
    st.pyplot(dummy_pie_chart("Pie Chart 5"))
    st.pyplot(dummy_pie_chart("Pie Chart 6"))
