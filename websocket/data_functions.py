import os
import pandas as pd
from django.conf import settings
import json


def display_all_date(path):
    # Read the data file into a DataFrame
    # Get the absolute file paths for your static files
    path = os.path.join(settings.STATIC_ROOT, path)
    df = pd.read_csv(path, sep=" ", header=None, names=["date", "time", "value"])
    
    # Combine date and time columns into a single datetime column
    df["datetime"] = pd.to_datetime(df["date"] + " " + df["time"])
    
    # Now, df contains three columns: "date", "time", and "value"
    # and one combined datetime column "datetime"
    
    # Convert the datetime column to strings
    datetime_list = df['datetime'].astype(str).to_list()
    
    # Return the datetime_list
    return datetime_list

def get_values_all(selected_date):
    path_light = os.path.join(settings.STATIC_ROOT, 'light.dat')
    path_humidity = os.path.join(settings.STATIC_ROOT, 'humidity.dat')
    path_temperature = os.path.join(settings.STATIC_ROOT, 'temperature.dat')
    df_light = pd.read_csv(path_light, sep=" ", header=None, names=["date", "time", "value"])
    df_temperature = pd.read_csv(path_temperature, sep=" ", header=None, names=["date", "time", "value"])
    df_humidity = pd.read_csv(path_humidity, sep=" ", header=None, names=["date", "time", "value"])

    # Combine date and time columns into a single datetime column
    df_light["datetime"] = pd.to_datetime(df_light["date"] + " " + df_light["time"])
    df_temperature["datetime"] = pd.to_datetime(df_temperature["date"] + " " + df_temperature["time"])
    df_humidity["datetime"] = pd.to_datetime(df_humidity["date"] + " " + df_humidity["time"])
    df_light["datetime"] = pd.to_datetime(df_light["date"] + " " + df_light["time"])

    # Convert the datetime column to strings
    datetime_list_light = df_light['datetime'].astype(str).to_list()
    datetime_list_temperature = df_temperature['datetime'].astype(str).to_list()
    datetime_list_humidity = df_humidity['datetime'].astype(str).to_list()

    response_data = {
        'humidity_value': None,
        'light_value': None,
        'temperature_value': None
    }

    for i in range(len(datetime_list_light)):
        if(datetime_list_light[i] == selected_date and datetime_list_temperature[i] == selected_date and datetime_list_humidity[i] == selected_date):
            response_data['humidity_value'] = df_humidity["value"][i].item()
            response_data['light_value'] = df_light["value"][i].item()
            response_data['temperature_value'] = df_temperature["value"][i].item()
            break  # Exit the loop once values are found
    return response_data