import pandas as pd
import matplotlib.pyplot as plt 

filename ="crypto_data.csv" 

try: 
    df= pd.read_csv(filename)

    df['extract_time'] = pd.to_datetime (df['extract_time'])

    available_coins = df['symbol'].unique()
    print("------------------------------------------------")
    print(f"Found data for :{available_coins}")
    print("------------------------------------------------")
   
    target_coin= input("Which coin do you want to see? (Type exactly as shown above): ")
   
    coin_data = df[df['symbol'] == target_coin]
    if coin_data.empty:
        print(f"Error: No data found for {target_coin}.check your spelling.")
    else:
        plt.figure(figsize=(10,5))
        

    plt.plot(coin_data['extract_time'],  coin_data['price'],
              marker='o', linestyle='-', color='b',label=target_coin)
    

    plt.title(f"{target_coin} Price history")
    plt.xlabel("Time")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()


    print("Opening graph...")
    plt.show()
except FileNotFoundError:
    print(f"Error:Could not find {filename}. check your folder to see what the csv is named.")

