# Bitcoin Analysis Project

## Projektübersicht

Dieses Projekt analysiert historische Bitcoin-Preise und verwendet eine SQLite-Datenbank zur effizienten Speicherung und Verwaltung der Daten. Die Daten werden verarbeitet, analysiert und visualisiert, um Einblicke in die Preisentwicklung von Bitcoin zu gewinnen.

## Setup-Anleitung

### Entwicklungsumgebung

1. **Python Installation**: Stellen Sie sicher, dass Python 3.8 oder höher auf Ihrem System installiert ist.
2. **Repository klonen**: Klonen Sie das Repository mit `git clone [https://github.com/Driton-Hajzeri/bitcoin-analysis.git]`.
3. **Abhängigkeiten installieren**: Installieren Sie die erforderlichen Python-Bibliotheken mit `pip install -r requirements.txt` aus dem Projektverzeichnis.

### Virtuelles Umfeld

Einrichtung eines virtuellen Umfelds zur Isolierung der Projektbibliotheken:

```sh
python -m venv venv
source venv/bin/activate  # Für Unix/MacOS
venv\Scripts\activate  # Für Windows
```


## Projektstruktur.     

BitcoinAnalysis/
│
├── scripts/
│ ├── fetch_data.py
│ ├── initialize_db.py
│ ├── process_data.py
│ ├── prepare_for_prophet.py
│ └── visualize.py
├── notebooks/
│ └── additional_analyses.ipynb
├── requirements.txt
├── .env
├── README.md
├── .gitignore
└── bitcoin_analysis.db

## Beschreibung der Komponenten

- `scripts/`: Enthält alle Python-Skripte des Projekts.
  - `fetch_data.py`: Ruft historische Bitcoin-Preise von einer API ab und speichert sie in der SQLite-Datenbank.
  - `initialize_db.py`: Erstellt die SQLite-Datenbank und die erforderlichen Tabellen.
  - `process_data.py`: Bereinigt und transformiert die rohen Daten in ein verarbeitbares Format.
  - `prepare_for_prophet.py`: Bereitet die verarbeiteten Daten für die Vorhersageanalyse vor.
  - `visualize.py`: Enthält Skripte zur Visualisierung der Daten und Vorhersagen.
- `notebooks/`: Enthält Jupyter Notebooks für explorative Analysen und interaktive Prototyping-Prozesse.
  - `additional_analyses.ipynb`: Notebook für zusätzliche Analysen.
- `requirements.txt`: Liste aller Python-Pakete, die für das Projekt benötigt werden.
- `.env`: Datei für Umgebungsvariablen, insbesondere sicherheitsrelevante Informationen wie API-Schlüssel.
- `README.md`: Eine Markdown-Datei, die eine Übersicht über das Projekt bietet.
- `.gitignore`: Regeln, um bestimmte Dateien oder Verzeichnisse nicht in das Git-Repository aufzunehmen.
- `bitcoin_analysis.db`: Die SQLite-Datenbank, die die historischen Bitcoin-Preisdaten enthält.

## Benutzeranleitung

### Datenbezug

- `fetch_data.py`: Ruft historische Bitcoin-Preise von einer API ab und speichert sie in der SQLite-Datenbank `bitcoin_analysis.db`.

### Datenverarbeitung

- `initialize_db.py`: Erstellt die SQLite-Datenbank und die Tabelle `bitcoin_prices`.
- `process_data.py`: Bereinigt und transformiert die rohen Daten in ein verarbeitbares Format und speichert sie in der Datenbank.
- `prepare_for_prophet.py`: Bereitet die verarbeiteten Daten für die Vorhersageanalyse vor und speichert sie in der Datenbank.

### Analyse und Visualisierung

- `visualize.py`: Verwendet die vorbereiteten Daten, um Vorhersagen zu generieren und diese visuell darzustellen. Die Ergebnisse werden in der interaktiven Umgebung (Jupyter Notebook) oder als Plotly-Graphen präsentiert.

### Ausführen der Skripte

Jedes Skript kann durch Ausführen des folgenden Befehls im Terminal gestartet werden, während das virtuelle Umfeld aktiv ist:

```sh
python scripts/<script_name>.py
```


## Architektur und Datenfluss

### Datenfluss

Die Daten fließen von der API in die SQLite-Datenbank (`bitcoin_analysis.db`). Die rohen Daten werden verarbeitet und bereinigt, bevor sie für die Analyse und Vorhersage vorbereitet werden. Nach der Analyse werden die Ergebnisse visualisiert.

### Komponenteninteraktion

Die Skripte interagieren durch den Zugriff auf die SQLite-Datenbank, die die Daten in verschiedenen Verarbeitungsstufen speichert und bereitstellt.

## Fazit und Ausblick

Das Projekt zeigt eine robuste Methode zur Analyse und Vorhersage von Bitcoin-Preisen unter Verwendung einer SQLite-Datenbank zur effizienten Datenverwaltung. Zukünftige Erweiterungen können Echtzeit-Datenverarbeitung, verbesserte Vorhersagemodelle oder die Integration von zusätzlichen Datenquellen umfassen, um die Vorhersagegenauigkeit zu erhöhen.

## Projekt-Dokumentation

### Einführung

Dieses Projekt zielt darauf ab, historische Bitcoin-Preisdaten zu analysieren und Vorhersagen über zukünftige Preisentwicklungen zu treffen. Es integriert eine SQLite-Datenbank zur effizienten Verwaltung und Speicherung der Daten.

### Projektstruktur

Detaillierte Übersicht über die Projektstruktur und die Funktionen der einzelnen Komponenten.

### Setup-Anleitung

Schritt-für-Schritt-Anleitung zur Einrichtung der Entwicklungsumgebung und Installation der erforderlichen Abhängigkeiten.

### Benutzeranleitung

Anleitung zur Nutzung der Skripte und Durchführung von Datenanalysen und Visualisierungen.

### Architektur und Datenfluss

Beschreibung des Datenflusses und der Interaktion zwischen den Komponenten des Projekts.

### Fazit und Ausblick

Zusammenfassung der Projektergebnisse und mögliche zukünftige Erweiterungen.
