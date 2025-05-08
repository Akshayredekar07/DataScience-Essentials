
import streamlit as st 
import pandas as pd 
import re
import matplotlib.pyplot as plt

st.set_page_config(layout='wide', page_title='StartUp Analysis')

df = pd.read_csv("startup_cleanded.csv")
# st.dataframe(df)


def laod_investor_details(investor):
    st.title(investor)
    # load the recent 5 investments of the investor 
    last5_df = df[df['investor'].str.contains(investor)].head()[['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader("Most recent investments")
    st.dataframe(last5_df)
    # Biggest investmnt

    col1, col2 = st.columns(2)
    with col1:
        big_series = df[df['investor'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.subheader("Biggest investments")
        fig, ax = plt.subplots()
        ax.bar(big_series.index, big_series.values)
        st.pyplot(fig)


    with col2:
        vertical_series = df[df['investor'].str.contains(investor)].groupby('vertical')['amount'].sum().plot(kind='pie')
        st.subheader("Sectors invested in")
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical_series)
        st.pyplot(fig1)



st.sidebar.title("Startup Funding Analysis")

option = st.sidebar.selectbox("Select One", ['Overall Analysis', 'StartUp', 'Investor'])

if option == "Overall Analysis":
    st.title("Overall Analysis")

elif option == "StartUp":
    st.sidebar.selectbox('Select Startup', sorted(df['startup'].unique()))
    btn1 = st.sidebar.button("Find startUp Details")

elif option == "Investor":
    selected_investor = st.sidebar.selectbox('Select Investor', sorted(set(df['investor'].str.split(',').sum())))
    btn2 = st.sidebar.button("Find startUp Details")
    if btn2:
        laod_investor_details(selected_investor)



