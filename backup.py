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

# Divide the page into two columns below the Excel file
left_col, right_col = st.columns(2)

with left_col:
   gender_cols = ['Male', 'Female']
gender_counts = df[gender_cols].sum()
gender_sizes = gender_counts.values
gender_labels = gender_counts.index.tolist()

# Age columns
#age_cols = ['Up-to 35 yrs old', '35-45 yrs old', '45+ yrs old']
#age_counts = df[age_cols].sum()
#age_sizes = age_counts.values
#age_labels = age_counts.index.tolist()

# Department columns
dept_cols = ['Sales & Marketing', 'R&D', 'Manufacturing', 'HR', 'Finance']
dept_counts = df[dept_cols].sum()
dept_sizes = dept_counts.values
dept_labels = dept_counts.index.tolist()

# Tenure columns
tenure_cols = ['0 - 6 months', '1 - 3 Years', '3 - 5 Years', '5 + years']
tenure_counts = df[tenure_cols].sum()
tenure_sizes = tenure_counts.values
tenure_labels = tenure_counts.index.tolist()

left_col, right_col = st.columns(2)

with left_col:
    st.markdown('<div class="custom-column-box">', unsafe_allow_html=True)

    # Gender Pie Chart (Assuming columns 2 and 3 are Male and Female)
    gender_cols = df.columns[1:3]
    gender_counts = df[gender_cols].sum()
    fig1, ax1 = plt.subplots()
    ax1.pie(gender_counts, labels=gender_cols, autopct='%1.1f%%', startangle=90)
    ax1.set_title("Gender Distribution")
    st.pyplot(fig1)

    st.markdown('</div>', unsafe_allow_html=True)
with right_col:
    st.markdown('<div class="custom-column-box">Right side content goes here.</div>', unsafe_allow_html=True)
