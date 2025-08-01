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


    .stColumns {
        gap: 40px !important; /* Increase gap between columns */
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
# Divide the page into two columns below the Excel file
# Demographics Section
st.markdown("## Demographic Breakdown")
col1, col2, col3 = st.columns(3)

# Column 1 — Gender
with col1:
    gender_cols = df.columns[1:3]
    gender_counts = df[gender_cols].sum()
    fig1, ax1 = plt.subplots(figsize=(2.5,2.5))
    ax1.pie(gender_counts, labels=gender_cols, autopct='%1.1f%%', startangle=90)
    ax1.set_title("Gender", fontsize=10)
    st.markdown('<div class="demographic-box">', unsafe_allow_html=True)
    st.pyplot(fig1)
    st.markdown('</div>', unsafe_allow_html=True)

    age_cols = df.columns[20:23]
    age_counts = df[age_cols].sum()
    fig3, ax3 = plt.subplots(figsize=(2.5,2.5))
    ax3.pie(age_counts, labels=age_cols, autopct='%1.1f%%', startangle=90)
    ax3.set_title("Age Group", fontsize=10)
    st.markdown('<div class="demographic-box">', unsafe_allow_html=True)
    st.pyplot(fig3)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    dept_cols = df.columns[8:13]
    dept_counts = df[dept_cols].sum()
    fig2, ax2 = plt.subplots(figsize=(2.5,2.5))
    ax2.pie(dept_counts, labels=dept_cols, autopct='%1.1f%%', startangle=90)
    ax2.set_title("Department", fontsize=10)
    st.markdown('<div class="demographic-box">', unsafe_allow_html=True)
    st.pyplot(fig2)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    tenure_cols = df.columns[16:20]
    tenure_counts = df[tenure_cols].sum()
    fig4, ax4 = plt.subplots(figsize=(2.5,2.5))
    ax4.pie(tenure_counts, labels=tenure_cols, autopct='%1.1f%%', startangle=90)
    ax4.set_title("Tenure", fontsize=10)
    st.markdown('<div class="demographic-box">', unsafe_allow_html=True)
    st.pyplot(fig4)
    st.markdown('</div>', unsafe_allow_html=True)
