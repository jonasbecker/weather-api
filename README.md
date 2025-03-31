# Wettervorhersage Anwendung
Es wird die Visual Crossing Weather API benutzt um eine Wettervorhersage für eine gegebene Anzahl von Tagen in einer json zu erhalten und in einem Diagramm visualisiert.

## Voraussetzungen

- Python 3.5 und höher
- Gewünschte Bibliotheken:
  - json 
  - requests 
  - datetime 
  - plotly 
  - pandas 

## Einsatz

- Legen Sie zuerst Ihren API-Schlüssel fest. Sie können einen Schlüssel von der Visual Crossing Weather API-Webseite erhalten.
- Definieren Sie Ihren Standort und die Anzahl der Tage, die Sie vorhersagen möchten.
- Führen Sie die Anwendung aus. 

## Funktionen

- `get_weather()`: Diese Funktion sendet eine GET-Anfrage an die Visual Crossing Weather API und gibt die Antwort als JSON-Objekt zurück.
- `save_weather_to_file(data, filename)`: Diese Funktion speichert das Wetterdaten-JSON-Objekt in eine Datei.
- `get_hourly_temp(data)`: Diese Funktion extrahiert die stündlichen Temperaturdaten aus den Wetterdaten.
- `get_daily_avg_temp(data)`: Diese Funktion extrahiert die täglichen Durchschnittstemperaturen aus den Wetterdaten.
- `plot_temperature(temperatures, title)`: Diese Funktion plottet die Temperaturdaten.

## Deployment

- Geben Sie Ihren Standort im Format 'Stadt, Land' ein.
- Geben Sie die Anzahl der Tage ein, die Sie vorhersagen möchten.
- Die Anwendung sendet eine Anfrage an die Visual Crossing Weather API, speichert die erhaltenen Daten und gibt sie als Diagramm aus.