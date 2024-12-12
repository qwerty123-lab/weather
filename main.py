from config import open_weather_token
import requests
from pprint import *

def get_weather(city, open_weather_token):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={open_weather_token}"
            )
        data = r.json()
        print(data)
    except Exception as ex:
        print(ex)
        print("Проверьте название города")

def main():
    city = input("Введите город: ")
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()