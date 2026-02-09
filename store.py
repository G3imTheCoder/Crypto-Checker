import pandas as pd
import os 

def save_to_csv(df, filename="crypto_data.csv"):
    """
    appends the dataframe to a CSV file. 
    If the file does not exist, it creates it with headers.
    """
    file_exists =os.path.isfile(filename) 

    df.to_csv(filename, mode='a', header=not file_exists, index=False)

    print(f"Data saved to {filename}")