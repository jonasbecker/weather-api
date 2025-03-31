import json
import requests
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta


API_KEY = "EYYDL6MQJAFR4PWX5YBE2EMYD"
LOCATION = input("Input 'City, Country' : ")
DAYS = int(input("Input the number of days: "))
DATE1 = datetime.today().strftime('%Y-%m-%d')
if DAYS <= 1:
    DATE2 = DATE1
else:
    DATE2 = (datetime.today() + timedelta(days=DAYS - 1)).strftime('%Y-%m-%d')

URL = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{LOCATION}/{DATE1}/{DATE2}?key={API_KEY}"


def get_weather():
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Status code: {response.status_code}")
        print(f"API Response: {response.text}")
        return {"error": "Request failed"}


def save_weather_to_file(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def get_hourly_temp(data):
    hourly_temp = []
    for day in data["days"]:
        for hour in day["hours"]:
            hourly_temp.append({"datetime": hour["datetime"], "temp": hour["temp"]})
    return hourly_temp


def get_daily_avg_temp(data):
    daily_temps = []
    for day in data["days"]:
        daily_temps.append({"datetime": day["datetime"], "temp": day["temp"]})
    return daily_temps


def plot_temperature(temperatures, title):
    df = pd.DataFrame(temperatures)
    df['datetime'] = pd.to_datetime(df['datetime'])
    fig = px.line(df, x='datetime', y='temp', title=title)
    fig.show()


def main():
    weather_data = get_weather()

    if 'error' in weather_data:
        print(weather_data['error'])
        return

    if DAYS < 7:
        temperatures = get_hourly_temp(weather_data)
        file_name = 'hourly_temperatures.json'
        title = f"Hourly temperatures for the next {DAYS} days"
    else:
        temperatures = get_daily_avg_temp(weather_data)
        file_name = 'daily_avg_temperatures.json'
        title = f"Daily average temperatures for the next {DAYS} days"

    save_weather_to_file(temperatures, file_name)
    print(f"Temperatures have been saved in '{file_name}'.")
    plot_temperature(temperatures, title)


if __name__ == '__main__':
    main()