import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")
uploaded_file = st.file_uploader("Choose a CV File", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

    # Simple Data Analysis
    st.subheader("Data Preview")
    st.write(df.head())


    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader(" Filter Data ")
    column = df.columns.tolist()
    selected_coloumns = st.selectbox("Select Columns to filter by", column)
    unique_values = df[selected_coloumns].unique()
    selected_value = st.selectbox("Select Value",unique_values)

    filtered_df = df[df[selected_coloumns] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_coloumn = st.selectbox("Select x_axis coloumn", column)
    y_coloumn = st.selectbox("Select y_axis coloumn", column)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_coloumn)[y_coloumn])
else:
    st.write("Please upload a CSV file to continue") 
    
