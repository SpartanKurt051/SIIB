import streamlit as st
import pandas as pd
# Provided values
employee_count = 100

file_path = 'SIIB.xlsx'
try:
    df = pd.read_excel(file_path)
    print("Column names:", df.columns.tolist())
except Exception as e:
    print("Error reading Excel file:", e)
