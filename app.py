import streamlit as st
import pandas as pd

# Load the Excel data
df = pd.read_excel('SIIB.xlsx')

# Show columns to help debug if needed
# st.write("Excel columns:", df.columns.tolist())

# Helper to get KPI score by metric name
def get_kpi_score(metric_name):
    row = df[df.iloc[:, 0] == metric_name]
    if not row.empty:
        return row.iloc[0, 1]
    else:
        return None

# Hardcoded Employee Count
employee_count = 100

# Strengths (descending)
strength_metrics = [
    'Engagement',
    'Customer Centricity',
    'Job and Work Environments',
    'Careers and Leadership Effectiveness'
]

strength_scores = {metric: get_kpi_score(metric) for metric in strength_metrics}
strength_scores = {k: v for k, v in strength_scores.items() if v is not None}
strength_scores_sorted = dict(sorted(strength_scores.items(), key=lambda item: item[1], reverse=True))

# Weaknesses (ascending)
weakness_metrics = [
    'Work Life Balance',
    'Performance & Rewards',
    'Diversity & Inclusion'
]

weakness_scores = {metric: get_kpi_score(metric) for metric in weakness_metrics}
weakness_scores = {k: v for k, v in weakness_scores.items() if v is not None}
weakness_scores_sorted = dict(sorted(weakness_scores.items(), key=lambda item: item[1]))

# Page styling: full width, good spacing between KPI columns
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
    .kpi-col {
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Employee Engagement Dashboard")

# Display KPIs - Strengths
kpi_cols = st.columns(len(strength_scores_sorted) + 1, gap="large")
kpi_cols[0].metric("Employee Count", employee_count)
for i, (metric, score) in enumerate(strength_scores_sorted.items()):
    kpi_cols[i+1].metric(metric, f"{score:.2f}")

# Display Weaknesses as a new row
st.markdown("### Areas to Improve")
weak_cols = st.columns(len(weakness_scores_sorted), gap="large")
for i, (metric, score) in enumerate(weakness_scores_sorted.items()):
    weak_cols[i].metric(metric, f"{score:.2f}")

# Optionally display the raw table for debugging
# st.dataframe(df)
