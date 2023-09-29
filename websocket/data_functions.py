import os
import pandas as pd
from django.conf import settings

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
