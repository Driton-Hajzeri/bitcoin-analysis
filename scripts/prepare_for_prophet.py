import pandas as pd
import sqlite3

def prepare_for_prophet():
    # Verbindung zur SQLite-Datenbank herstellen
    conn = sqlite3.connect('bitcoin_analysis.db')
    
    # Daten laden
    df = pd.read_sql('SELECT * FROM bitcoin_prices', conn)
    
    # Spalten umbenennen
    df.rename(columns={'time': 'ds', 'close': 'y'}, inplace=True)
    
    # Daten zurück in die Datenbank speichern
    df.to_sql('prophet_ready', conn, if_exists='replace', index=False)
    conn.close()
    
    print("Data prepared for Prophet and saved to 'bitcoin_analysis.db'")

if __name__ == '__main__':
    prepare_for_prophet()
