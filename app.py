import streamlit as st
import pandas as pd

# Load data from your excel sheet
df = pd.read_excel('SIIB.xlsx')

# Replace these with the actual column names in your sheet
# This is a template; adjust as needed!
employee_count = 100

# Assuming the following columns in your sheet:
# 'Overall Engagement', 'Customer Centricity', 'Job and Work Environments',
# 'Careers and Leadership Effectiveness', 'Work Life Balance',
# 'Performance & Rewards', 'Diversity & Inclusion'

kpi_strengths = [
    'Engagement',
    'Customer Centricity',
    'Job and Work Environments',
    'Careers',
    'Leadership Effectiveness'
]
strengths_sorted = df[kpi_strengths].mean().sort_values(ascending=False)

kpi_weaknesses = [
    'Work Life Balance',
    'Performance & Rewards',
    'Diversity & Inclusion'
]
weaknesses_sorted = df[kpi_weaknesses].mean().sort_values(ascending=True)

st.title("Dashboard KPIs")

# KPI indicators at the top in columns
kpi_cols = st.columns(6)
kpi_cols[0].metric("Employee Count", employee_count)

# Add strengths sorted descending
for idx, (kpi, value) in enumerate(strengths_sorted.items()):
    kpi_cols[idx+1].metric(kpi, f"{value:.2f}")

# If you want the weaknesses displayed as well, add another row:
st.subheader("Weaknesses")
weak_cols = st.columns(3)
for idx, (kpi, value) in enumerate(weaknesses_sorted.items()):
    weak_cols[idx].metric(kpi, f"{value:.2f}")
