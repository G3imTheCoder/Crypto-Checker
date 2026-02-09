import streamlit as st
import pandas as pd


st.set_page_config(page_title="Crypto Dashboard", layout="wide")
st.title(" Live Crypto Tracker")


filename = "data.csv"

try:
    df = pd.read_csv(filename)
    df['extract_time'] = pd.to_datetime(df['extract_time'])
    
    
    if df.empty:
        st.error("The CSV is empty. Please let main.py collect more data!")
    else:
        
     
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.subheader(" Market Stats")
            
        
            latest_data = df.groupby('symbol').tail(1)[['symbol', 'price']]
            
            
            stats = df.groupby('symbol')['price'].agg(['min', 'max', 'mean'])
            
            
            st.dataframe(stats)
            
           
            stats['volatility'] = stats['max'] - stats['min']
            most_volatile = stats['volatility'].idxmax()
            st.info(f" Most Volatile: **{most_volatile}**")

        with col2:
            st.subheader(" Price History")
            
         
            coin_list = df['symbol'].unique()
            selected_coin = st.selectbox("Select a coin to view:", coin_list)
            
           
            coin_data = df[df['symbol'] == selected_coin]
         
            st.line_chart(coin_data.set_index('extract_time')['price'])
            
       
        if st.button(' Refresh Data'):
            st.rerun()

except FileNotFoundError:
    st.error(f"Waiting for {filename} to be created... Run main.py!")