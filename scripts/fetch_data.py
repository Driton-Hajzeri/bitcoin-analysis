import requests
import pandas as pd
from dotenv import load_dotenv
import os
import sqlite3

def fetch_market_data():
    load_dotenv()
    api_key = os.getenv('CRYPTO_COMPARE_API_KEY')
    url = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=2000&api_key={api_key}'
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200 and 'Data' in data:
        df = pd.DataFrame(data['Data']['Data'])
        
        # Verbindung zur SQLite-Datenbank herstellen
        conn = sqlite3.connect('bitcoin_analysis.db')
        df.to_sql('bitcoin_prices', conn, if_exists='replace', index=False)
        conn.close()
        
        print("Market data saved to 'bitcoin_analysis.db'")
    else:
        raise Exception("Error fetching market data")

if __name__ == '__main__':
    fetch_market_data()
