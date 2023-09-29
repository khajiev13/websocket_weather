import json
import os
from channels.generic.websocket import WebsocketConsumer

from .data_functions import display_all_date

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()


        # Send JSON data with file paths
        data = display_all_date('humidity.dat')
        self.send(json.dumps({'data': data}))


# Check if the files exist
# if os.path.isfile('/Users/khajievroma/Desktop/Python/weather_websocket/static_data/humidity.dat'):
#     print("Humidity file exists.")
# else:
#     print("Humidity file does not exist.")
