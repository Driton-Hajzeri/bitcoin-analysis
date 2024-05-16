import requests
import pandas as pd
from dotenv import load_dotenv
import os
import sqlite3

def fetch_market_data():
    # Umgebungsvariablen aus der .env Datei laden
    load_dotenv()
    
    # API-Schlüssel für die Crypto Compare API aus den Umgebungsvariablen abrufen
    api_key = os.getenv('CRYPTO_COMPARE_API_KEY')
    
    # URL für die API-Anfrage definieren, einschließlich des API-Schlüssels
    url = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=2000&api_key={api_key}'
    
    # API-Anfrage senden
    response = requests.get(url)
    
    # Antwortdaten im JSON-Format parsen
    data = response.json()
    
    # Überprüfen, ob die Anfrage erfolgreich war und die erwarteten Daten enthält
    if response.status_code == 200 and 'Data' in data:
        # Daten in einen Pandas DataFrame umwandeln
        df = pd.DataFrame(data['Data']['Data'])
        
        # Verbindung zur SQLite-Datenbank herstellen (bzw. erstellen, falls sie noch nicht existiert)
        conn = sqlite3.connect('bitcoin_analysis.db')
        
        # DataFrame in die Datenbanktabelle 'bitcoin_prices' schreiben, vorhandene Tabelle ersetzen
        df.to_sql('bitcoin_prices', conn, if_exists='replace', index=False)
        
        # Datenbankverbindung schließen
        conn.close()
        
        print("Market data saved to 'bitcoin_analysis.db'")
    else:
        # Fehler auslösen, falls die Daten nicht erfolgreich abgerufen wurden
        raise Exception("Error fetching market data")

if __name__ == '__main__':
    # Funktion aufrufen, um Marktdaten abzurufen und in die Datenbank zu speichern
    fetch_market_data()

