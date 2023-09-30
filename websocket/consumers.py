import json
import os
from channels.generic.websocket import WebsocketConsumer

from .data_functions import display_all_date, get_values_all

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        # Send JSON data with file paths
        data = display_all_date('humidity.dat')
        self.send(json.dumps({'data': data}))

    def receive(self, text_data):
        # Parse the incoming JSON message
        message_data = 0
        try:
            message_data = json.loads(text_data)
        except json.JSONDecodeError:
            message_data = {}
        selected_date = message_data['selected_date']
        three_values = get_values_all(selected_date)
        self.send(json.dumps(three_values))

    def disconnect(self, close_code):
        # Perform cleanup tasks when a client disconnects
        # For example, you can log the disconnection
        print(f"WebSocket connection closed with code: {close_code}")

# Check if the files exist
# if os.path.isfile('/Users/khajievroma/Desktop/Python/weather_websocket/static_data/humidity.dat'):
#     print("Humidity file exists.")
# else:
#     print("Humidity file does not exist.")
