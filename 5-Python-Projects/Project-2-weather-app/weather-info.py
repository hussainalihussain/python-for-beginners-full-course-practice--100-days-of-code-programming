import requests
import json
import pyttsx3
import os
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv('WEATHER_API_KEY')
weather_api_url=os.getenv('WEATHER_API_URL')
voice_speed_rate=os.getenv('VOICE_SPEED_RATE')

city = input('Enter the name of city:\n')
url = f'{weather_api_url}?key={api_key}&q={city}'

response = requests.get(url)
response_dictionary = json.loads(response.text)

engine = pyttsx3.init()

textToSpeech = f"The weather of {response_dictionary['location']['name']} is {response_dictionary['current']['temp_c']} centigrade"

engine.setProperty('rate', voice_speed_rate)
engine.say(textToSpeech)
engine.runAndWait()