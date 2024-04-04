from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class GetWeather(Action):
    def name(self) -> Text:
        return "action_get_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        if tracker.latest_message['entities']:
            city = tracker.latest_message['entities'][0]['value']
            response = requests.get(f"https://api.weather.com/weather/{city}")
            weather_data = response.json()
            dispatcher.utter_message(text=f"The weather in {city} is {weather_data['weather']}")

        else:
            dispatcher.utter_message(text="I couldn't detect the city name in your message.")

        return []
    