import yfinance as yf
import pandas as pd
from datetime import datetime 

def get_price(symbol): 
    print(f"Fetching data for {symbol}...")

    ticker = yf.Ticker(symbol)
    data =ticker.history(period="5d")

    if data.empty: 
        print(f"No data found.")
        return None
    
    latest_price = data['Close'].iloc[-1]

    df =  pd.DataFrame({
        "symbol": [symbol],
        "extract_time": [datetime.now()],
        "price": [latest_price]
        
    })
    return df 
