import requests

API_KEY = "YOUR_API_KEY"  # Get one for free at https://openweathermap.org/api
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code != 200 or data.get("cod") != 200:
        print("❌ Error: Could not fetch weather for that city.")
        return

    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    print(f"\n🌎 Weather in {city.title()}:")
    print(f"🌡️ Temperature: {temp}°C")
    print(f"☁️ Condition: {weather}")
    print(f"💧 Humidity: {humidity}%\n")

def main():
    print("== Simple Weather Fetcher ==")
    city = input("Enter a city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()
