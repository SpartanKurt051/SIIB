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

 .custom-column-box {
       border: 2px solid #cccccc;
        border-radius: 14px;
        padding: 24px 12px;
        background: rgba(0,0,0,0); /* Transparent background */
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 200px;
        height: 100%;
        margin-bottom: 18px;
        margin-left: 8px;
        margin-right: 8px;
        text-align: center;
    }

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
st.write(df)

engagement_row = df[df.iloc[:, 0] == 'Engagement']
females_score = engagement_row['Female'].values[0]
executive_score = engagement_row['Executive'].values[0]

# Existing code
st.write(df)

# Divide the page into two columns below the Excel file
left_col, right_col = st.columns(2)

with left_col:
    st.markdown('<div class="custom-column-box">', unsafe_allow_html=True)

    # Gender Pie Chart
    gender_counts = df[['Male', 'Female']].sum()
    gender_labels = gender_counts.index.tolist()
    gender_sizes = gender_counts.values
    fig1, ax1 = plt.subplots(figsize=(1.3, 1.3))
    ax1.pie(gender_sizes, labels=gender_labels, autopct='%1.1f%%', startangle=90)
    ax1.set_title("Gender", fontsize=10)
    st.pyplot(fig1, use_container_width=False)

    # Age Pie Chart
    age_cols = ['Up-to 35 yrs old', '35-45 yrs old', '45+ yrs old']
    age_counts = df[age_cols].sum()
    age_labels = age_counts.index.tolist()
    age_sizes = age_counts.values
    fig2, ax2 = plt.subplots(figsize=(1.3, 1.3))
    ax2.pie(age_sizes, labels=age_labels, autopct='%1.1f%%', startangle=90)
    ax2.set_title("Age", fontsize=10)
    st.pyplot(fig2, use_container_width=False)

    # Department Pie Chart
    dept_cols = ['Sales & Marketing', 'R&D', 'Manufacturing', 'HR', 'Finance']
    dept_counts = df[dept_cols].sum()
    dept_labels = dept_counts.index.tolist()
    dept_sizes = dept_counts.values
    fig3, ax3 = plt.subplots(figsize=(1.3, 1.3))
    ax3.pie(dept_sizes, labels=dept_labels, autopct='%1.1f%%', startangle=90)
    ax3.set_title("Department", fontsize=10)
    st.pyplot(fig3, use_container_width=False)

    # Tenure Pie Chart
    tenure_cols = ['0 - 6 months', '1 - 3 Years', '3 - 5 Years', '5 + years']
    tenure_counts = df[tenure_cols].sum()
    tenure_labels = tenure_counts.index.tolist()
    tenure_sizes = tenure_counts.values
    fig4, ax4 = plt.subplots(figsize=(1.3, 1.3))
    ax4.pie(tenure_sizes, labels=tenure_labels, autopct='%1.1f%%', startangle=90)
    ax4.set_title("Tenure", fontsize=10)
    st.pyplot(fig4, use_container_width=False)

    st.markdown('</div>', unsafe_allow_html=True)
with right_col:
    st.markdown('<div class="custom-column-box">Right side content goes here.</div>', unsafe_allow_html=True)

