import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# Provided values
employee_count = 100

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
        padding-top: 100px;
        padding-bottom: 100px;
        padding-left: 10px;
        padding-right: 10px;
        width: 1500px;
        max-width: 1500px;
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

df = pd.read_excel('SIIB.xlsx')
df = df.iloc[:, 2:]
st.write(df)

engagement_row = df[df.iloc[:, 0] == 'Engagement']
females_score = engagement_row['Female'].values[0]
executive_score = engagement_row['Executive'].values[0]

# Existing code
st.write(df)

# Divide the page into two columns below the Excel file
left_col, right_col = st.columns(2)

with left_col:
    st.write("Left side content goes here.")

with right_col:
    st.write("Right side content goes here.")

