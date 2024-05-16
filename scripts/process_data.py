import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import sqlite3

def process_data():
    # Verbindung zur SQLite-Datenbank herstellen
    conn = sqlite3.connect('bitcoin_analysis.db')
    
    # Daten laden
    df = pd.read_sql('SELECT * FROM bitcoin_prices', conn)
    
    # Zeitstempel konvertieren
    df['time'] = pd.to_datetime(df['time'], unit='s')
    
    # Normalisieren der Preisdaten
    scaler = MinMaxScaler()
    df['normalized_price'] = scaler.fit_transform(df[['close']])
    
    # Verarbeitete Daten zurück in die Datenbank speichern
    df.to_sql('bitcoin_prices', conn, if_exists='replace', index=False)
    conn.close()
    
    print("Processed data saved to 'bitcoin_analysis.db'")

if __name__ == '__main__':
    process_data()
