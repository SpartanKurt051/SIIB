import streamlit as st
import pandas as pd
# Provided values
employee_count = 100

file_path = 'SIIB.xlsx'
df = pd.read_excel(file_path)
print(df)
# Print the column names
print("Column names:", df.columns.tolist())

strength_scores = {
    'Customer Centricity': 96,
    'Job and Work Environments': 92,
    'Engagement': 89,
    'Careers': 86,
    'Leadership Effectiveness': 85
}

weakness_scores = {
    'Work Life Balance': 74,
    'Performance & Rewards': 76,
    'Diversity & Inclusion': 82
}

# Sort scores
strength_scores_sorted = dict(sorted(strength_scores.items(), key=lambda item: item[1], reverse=True))
weakness_scores_sorted = dict(sorted(weakness_scores.items(), key=lambda item: item[1]))

# Page styling: full width, spacing
st.markdown("""
    <style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        padding-left: 2rem;
        padding-right: 2rem;
        width: 100vw;
        max-width: 100vw;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Employee Engagement Dashboard")

# Display KPIs - Strengths
kpi_cols = st.columns(len(strength_scores_sorted) + 1, gap="large")
kpi_cols[0].metric("Employee Count", employee_count)
for i, (metric, score) in enumerate(strength_scores_sorted.items()):
    kpi_cols[i+1].metric(metric, f"{score}")

# Display Weaknesses as a new row
st.markdown("### Areas to Improve")
if len(weakness_scores_sorted) > 0:
    weak_cols = st.columns(len(weakness_scores_sorted), gap="large")
    for i, (metric, score) in enumerate(weakness_scores_sorted.items()):
        weak_cols[i].metric(metric, f"{score}")
else:
    st.info("No weakness KPIs found.")
    

