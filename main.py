from extract import get_price
from store import save_to_csv
from notification import send_email
import pandas as pd
import time

coins = ["BTC-USD", "ETH-USD", "SOL-USD", "BNB-USD"]

last_alert = {} 

COOLDOWN_SECONDS = 3600 

print(f"🚀 Tracking started for {coins}...")

while True:
    for coin in coins:
        new_data = get_price(coin)
        
        if new_data is not None:
            save_to_csv(new_data)
            
            # --- TRADING ALGORITHM ---
            history = pd.read_csv("crypto_data.csv")
            coin_history = history[history['symbol'] == coin]
            
            if len(coin_history) >= 5:
                last_5_avg = coin_history['price'].tail(5).mean()
                current_price = new_data['price'].iloc[0]
                
                # Check for DIP (0.5% drop)
                if current_price < last_5_avg * 0.995:
                    
                    
                    current_time = time.time()
                    
                    
                    if coin not in last_alert or (current_time - last_alert[coin] > COOLDOWN_SECONDS):
                        
                        print(f"📉 DIP DETECTED for {coin}! Sending email...")
                        subject = f"ALERT: {coin} Price Drop!"
                        body = f"Price dropped to ${current_price:.2f}. Average was ${last_5_avg:.2f}. Time to buy?"
                        
                        send_email(subject, body)
                        
                        # Update the last alert time
                        last_alert[coin] = current_time
                    else:
                        print(f"📉 {coin} is down, but email skipped (Cooldown active)")

        else:
            print(f"Failed to fetch {coin}")
            
    print("Waiting 60 seconds...")
    time.sleep(60)