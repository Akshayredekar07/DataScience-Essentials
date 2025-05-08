import streamlit as st
import pandas as pd 


gender = st.selectbox('Select gender', ['male', 'female', 'other'])
email = st.text_input('Enter email')
password = st.text_input('Enter password')

btn = st.button('Login Karo')

if btn:
    if email == 'akshay@gmail.com' and password == 'akshay':
        st.write(gender)
        st.balloons()
    else:
        st.error("Login Failed")
        


# file uploader

file= st.file_uploader('Upload file')

if file is not None:
    df=pd.read_csv(file, encoding='ISO-8859-1')  # Specify encoding to handle non-UTF-8 files
    st.dataframe(df.describe())
