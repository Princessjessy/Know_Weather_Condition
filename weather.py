from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def know_current_weather(town="Topeka Town"):

    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={town}&units=imperial'

    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    print('\n*** Know Current Weather Conditions ***\n')

    town = input("\nPlease enter a town name: ")

    weather_data = know_current_weather(town)

    print("\n")
    pprint(weather_data)
