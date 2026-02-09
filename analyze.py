import pandas as pd 

filename ="crypto_data.csv" 

try : 
    df = pd.read_csv(filename)
   
    if df.empty:
        print("The file is empty! Let main.py run for a while first.")
        exit()
  
    stats = df.groupby('symbol')['price'].agg(['count', 'min', 'max', 'mean'])

    
    stats['volatility'] = stats['max'] - stats['min']

    pd.options.display.float_format = '{:.2f}'.format

    print("\n" + "="*50)
    print(" CRYPTO MARKET REPORT ")
    print("="*50)
    print(stats)
    print("\n")
    
    # 6. Find the winner
    most_volatile = stats['volatility'].idxmax()
    highest_volatility = stats['volatility'].max()
    
    print(f" Most Volatile Coin: {most_volatile} (Moved ${highest_volatility:.2f})")


except FileNotFoundError:
    print("Error: crypto_data.csv not found. Run main.py first!")