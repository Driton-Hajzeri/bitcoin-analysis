import sqlite3

def initialize_database():
    # Verbindung zur SQLite-Datenbank herstellen
    conn = sqlite3.connect('bitcoin_analysis.db')
    cursor = conn.cursor()

    # Tabelle erstellen
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bitcoin_prices (
            time TIMESTAMP PRIMARY KEY,
            close REAL,
            high REAL,
            low REAL,
            open REAL,
            volumefrom REAL,
            volumeto REAL,
            normalized_price REAL
        )
    ''')

    # Änderungen speichern und Verbindung schließen
    conn.commit()
    conn.close()

if __name__ == '__main__':
    initialize_database()
