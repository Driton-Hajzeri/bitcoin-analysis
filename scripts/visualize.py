import pandas as pd
from prophet import Prophet
import plotly.graph_objs as go
import sqlite3

# Verbindung zur SQLite-Datenbank herstellen
conn = sqlite3.connect('bitcoin_analysis.db')

# Daten laden
df = pd.read_sql('SELECT ds, y FROM prophet_ready', conn)
conn.close()

# Überprüfen der ersten Zeilen, um die Datenstruktur zu sehen
print(df.head(3))

# Konvertieren des Datentyps der 'ds' Spalte zu datetime
df['ds'] = pd.to_datetime(df['ds'])

# Modell erstellen und anpassen
model = Prophet()
model.fit(df)

# Zukunftsvorhersage erstellen
future = model.make_future_dataframe(periods=365)  # Für ein Jahr
forecast = model.predict(future)

# Vorhersage visualisieren
fig = go.Figure()

# Tatsächliche Daten
fig.add_trace(go.Scatter(x=df['ds'], y=df['y'], mode='markers', name='Actual'))

# Vorhersagelinie
fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], mode='lines', name='Predicted'))

# Unsicherheitsbereiche
fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_upper'], fill=None, mode='lines', line=dict(color='gray'), showlegend=False))
fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_lower'], fill='tonexty', mode='lines', line=dict(color='gray'), showlegend=False))

# Layout anpassen
fig.update_layout(title='Bitcoin Price Prediction', xaxis_title='Date', yaxis_title='Price', hovermode='x')

# Plot anzeigen
fig.show()
