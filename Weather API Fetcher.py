from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv("API_KEY")

print("\nWelcome to the Weather API Fetcher!\nYou can get the current weather information for any city by entering its name.\n")

try:
    city = input("Enter city: ")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    data = response.json()
    print(f"Temperature: {data["main"].get("temp")} K")
    print(f"Weather description: {data.get("weather", [{}])[0].get("description")}")
    print(f"Humidity: {data["main"].get("humidity")}%")
except:
    print("An error occurred while fetching the weather data. Ensure that the city name is correct and your internet connection is stable. Please try again.")
