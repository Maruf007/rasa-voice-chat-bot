# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd
import re

class ActionSearchResult(Action):

		def name(self) -> Text:
			return "action_search_results"

		def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

			category = tracker.get_slot('category')
			try:
				price = int(re.findall(r'[0-9]+',tracker.get_slot('price'))[0])
			except:
				price = 0
			try:
				ram = int(re.findall(r'[0-9]+',tracker.get_slot('ram'))[0])
			except:
				ram = 0
			try:
				camera = int(re.findall(r'[0-9]+',tracker.get_slot('camera'))[0])
			except:
				camera = 0
			df = pd.read_csv('C:\Source_Code\conversational-ai\RasaVoiceBot\\actions\phones_laptops_database.csv')

			output = []
			output.append({'product_url': 'https://support.apple.com/library/content/dam/edam/applecare/images/en_US/iphone/iphone-14-pro-max-colors.png'})
			if category == 'phone':
				output = df[(df['category']=='phone') & (df['price_usd'] <= price) & (df['back_camera_megapixel'] >= camera)]
			elif category == 'laptop':
				output = df[(df['category']=='laptop') & (df['price_usd'] <= price) & (df['ram'] >= ram)]

			for url in output['product_url']:
				dispatcher.utter_message(image=url)

			return []