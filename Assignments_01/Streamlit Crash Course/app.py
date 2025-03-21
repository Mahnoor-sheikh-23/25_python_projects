import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from textblob import TextBlob
import nltk
from PIL import Image
import sqlite3
import os

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home 🏡 ", "Data Dashboard 📊 ", "Text Analyzer 🔍 ", "Stock Tracker 🚫 ", "🖼️ Image Classifier", "Library Manager 📚"])

# Home Page
import streamlit as st

if page == "Home 🏡 ":
    st.title("📊 Multi-Feature Streamlit Dashboard")
    
    # About Me Section
    st.subheader("👨‍💻 About Me")
    st.write("""
        Hello! My name is Mahnoor , and I am passionate about data science and software development. 
        I specialize in building interactive web applications using Python and Streamlit, focusing on 
        data visualization, machine learning, and data management. This project showcases my skills and 
        provides useful tools to solve real-world problems.

        In this dashboard, you'll find various features to help analyze and visualize data in engaging ways. 
        Whether it's tracking stock prices or classifying images, this platform offers a comprehensive experience 
        for anyone looking to explore these functionalities.
    """)

    # App Description
    st.subheader("📝 About the App")
    st.write("""
        The **Multi-Feature Streamlit Dashboard** is a collection of tools and functionalities for data analysis, 
        visualization, and machine learning. The goal is to provide a simple and intuitive interface for various 
        tasks useful for anyone working with data or looking to interact with data creatively.

        ### 🚀 Features:
        - **📊 Data Visualization**: Create beautiful, interactive charts and graphs to visualize data insights.
        - **📝 Natural Language Processing (NLP)**: Use powerful NLP techniques to analyze text, extract keywords, and more.
        - **📈 Stock Tracking**: Track and visualize stock prices in real-time. Get the latest data and analyze market trends.
        - **🖼️ Image Classification**: Classify images using machine learning models. Upload your own images and see the model's performance.
        - **📚 Library Management**: Manage your library by adding, updating, and deleting books. Keep track of what you own and want to read.

        ### 🌟 Why This App?
        This app is designed to be a one-stop solution for anyone looking to work with data or build interactive 
        web applications. Streamlit allows me to quickly turn Python code into beautiful web applications with minimal effort. 
        Each feature is crafted to provide the best user experience while maintaining simplicity and efficiency.

        Enjoy exploring the app and feel free to reach out if you have any questions!
    """)
    



# Data Dashboard
elif page == "Data Dashboard 📊 ":
    st.title("📈 Data Dashboard")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("### Data Preview")
        st.dataframe(df.head())
        st.write("### Data Summary")
        st.write(df.describe())
        st.write("### Data Visualization")
        column = st.selectbox("Select a column for visualization", df.columns)
        plt.figure(figsize=(8, 5))
        plt.hist(df[column], bins=20, color='skyblue', edgecolor='black')
        st.pyplot(plt)

# Text Analyzer
elif page == "Text Analyzer 🔍 ":
    st.title("📝 Text Analysis")
    user_text = st.text_area("Enter text")
    if st.button("Analyze"):
        blob = TextBlob(user_text)
        st.write("**Sentiment Analysis:**", blob.sentiment)
        words = nltk.word_tokenize(user_text)
        word_freq = pd.Series(words).value_counts()
        st.bar_chart(word_freq)

# Stock Price Tracker
elif page == "Stock Tracker 🚫 ":
    st.title("📊 Stock Price Tracker")
    stock_ticker = st.text_input("Enter Stock Symbol (e.g., AAPL)")
    if st.button("Get Stock Data"):
        stock = yf.Ticker(stock_ticker)
        stock_hist = stock.history(period="1mo")
        st.line_chart(stock_hist['Close'])

# Image Classifier (Dummy Implementation)
elif page == "🖼️ Image Classifier":
    st.title("🖼️ Image Classifier")
    uploaded_img = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])
    if uploaded_img is not None:
        image = Image.open(uploaded_img)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        st.write("🔍 Dummy Prediction: This is an example image!")

# Library Manager
elif page == "Library Manager 📚":
    st.title("📚 Library Management System")
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT)")
    st.write("### Add a Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    if st.button("Add Book"):
        cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
        conn.commit()
        st.success("Book Added Successfully")
    st.write("### Book List")
    books = pd.read_sql("SELECT * FROM books", conn)
    st.dataframe(books)
    conn.close()
