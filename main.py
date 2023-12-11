import requests
from datetime import datetime
import os

# user_input = input("Tell me which excersices you did: ")
user_input = "i run for 4km"
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEETY_BEARER_TOKEN = os.environ.get("SHEETY_BEARER_TOKEN")

EXERCISE_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
ADD_ROW = "https://api.sheety.co/4762a863c90382f33ad96aab1a6b81ed/myWorkouts/workouts"
sheety_headers = {
    "Authorization": SHEETY_BEARER_TOKEN
}

nutri_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

body = {
    "query": user_input
}

exercise_response = requests.post(url=EXERCISE_URL, json=body, headers=nutri_headers)
exercise_response.raise_for_status()

exercise_data = exercise_response.json()

exercise_type = exercise_data["exercises"][0]["name"]
duration = exercise_data["exercises"][0]["duration_min"]
calories = exercise_data["exercises"][0]["nf_calories"]
date = datetime.now()

exercise_params = {
    "workout": {
        "date": date.strftime("%d/%m/%Y"),
        "time": date.strftime("%H:%M:%S"),
        "exercise": exercise_type.title(),
        "duration": int(duration),
        "calories": int(calories)
    }
}
add_row_response = requests.post(url=ADD_ROW, json=exercise_params, headers=sheety_headers)

