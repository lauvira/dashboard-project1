import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Hi! Welcome to My First Data Analysis Project ^^')
st.header('Datased Used: E-Commerce Public Dataset')
with st.expander("See explanation"):
    st.write(
        """The dataset used is a Brazilian ecommerce public dataset of orders made at Olist Store.
        The dataset has information of 100k orders from 2016 to 2018 made at multiple marketplaces in Brazil.
        Its features allows viewing an order from multiple dimensions: from order status, price, payment and
        freight performance to customer location, product attributes and finally reviews written by customers.
        They also released a geolocation dataset that relates Brazilian zip codes to lat/lng coordinates.

        URL : https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
        """
    )

tab1, tab2 = st.tabs(["Analysis 1", "Analysis 2"])
 
with tab1:
    st.header("What is the trend of order status from 2016 to 2018?")
    st.text("""To answer this question, I used 'order status' and its timestamp.
Here is an example of the data used:""")
    df = pd.DataFrame({
    'order_status': ['delivered', 'canceled', 'shipping', 'invoiced'],
    'order_month': ['2018-01', '2017-05', '2016-12', '2017-10'],
})
    st.dataframe(data=df, width=500, height=150)
    st.text("""The result of my analysis is:""")
    with st.expander("Conclusion"):
        st.write(
        """Unfortunately, I still confused on how to make a line chart here :). Biggest apologize.""")
 
with tab2:
    st.header("Which sellers were the “top sellers” during 2016-2018?")
    st.text("""To answer this question, I used order id, order score, and the seller id.""")
    st.text("""The result of my analysis is:""")

    X = ['6560....', 'cc41....', '4a3c....', '1f50....', 'da86....']
    Y = [7245, 6969, 6869, 5788, 5482]

    fig, ax = plt.subplots()
    ax.bar(X, Y)

    st.pyplot(fig)

    with st.expander("Conclusion"):
        st.write(
        """The objective of this analysis is to identify the Top Sellers.
        \n The initial thought is as follows:
        \n \t If a seller has a high score, their options may include:
        \n 1. A lot of orders with varying ratings (indicating good products and service).
        \n 2. A very high volume of orders but average or low ratings (usually selling inexpensive items of average or lower quality, yet still purchased due to necessity).
        \n 3. Few orders but all ratings are high (indicating the sale of high-quality products).
        
        \n \t However, regardless of these factors, the seller has made a significant contribution to this e-commerce platform.

    \n Several outcomes may arise from the Top Sellers data:
    \n 1. Awarding bonuses.
    \n 2. Granting a "Recommended Seller" tag.
    \n 3. Ultimately, this may foster a sense of healthy competition among sellers, encouraging them to enhance quality, promote their products, etc.
        """
    )
    

st.caption('by Laurensia Vira Farindra 2024')