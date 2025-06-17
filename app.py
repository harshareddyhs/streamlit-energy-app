import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("My Streamlit Energy App")

uploaded_file = st.file_uploader("Upload your Energy CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Preview of Uploaded Data", df.head())

    st.write("### Summary Statistics")
    st.write(df.describe())

    st.write("### Line Chart")
    st.line_chart(df.select_dtypes(include='number'))
else:
    st.warning("Please upload a CSV file to proceed.")
