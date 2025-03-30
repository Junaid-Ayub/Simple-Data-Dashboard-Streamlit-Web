import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Simple Data Dashboard!")
file = st.file_uploader("Choose a CSV File", type='csv')

if file is not None:
    df = pd.read_csv(file)

    st.header("Data Preview")
    st.write(df.head())

    st.header("Data Summary")
    st.write(df.describe())

    st.header("Filter Data")

    columns = df.columns.tolist()
    selected_columns = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_columns].unique()
    selected_values = st.selectbox("Select Value", unique_values)
    filtered_dataframe = df[df[selected_columns] == selected_values]

    if st.button("Display Filtered Data"):
        st.write(filtered_dataframe)

    st.header("Plot Data")

    x_column = st.selectbox("Select x-axis Column", columns)
    y_column = st.selectbox("Select y-axis Column", columns)

    if st.button("Plot the Data"):
        st.line_chart(filtered_dataframe.set_index(x_column)[y_column])

else:
    st.write("Waiting on file upload...")

