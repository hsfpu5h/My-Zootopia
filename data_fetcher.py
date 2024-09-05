import os
import requests

def fetch_data(animal_name):
    api_key = os.getenv('API_NINJAS_KEY')
    api_url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    response = requests.get(api_url, headers={"X-Api-Key": api_key})
    if response.status_code == 200:
        try:
            data = response.json()
            if data:
                return data
        except Exception as error:
            print(f"Error: {error}")
    return None