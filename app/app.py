import logging
from typing import Dict, Any
from dotenv import load_dotenv

from dto import WeatherData
from Collection import RequestApi

load_dotenv()

class App(object):

    def __init__(self) -> None:
        self._logging = logging.getLogger(self.__class__.__name__)
        self._request_api: RequestApi = RequestApi()
    
    def get_temp_of_city(self, city: str) -> Dict[str, Any]:
        temp_data = self._request_api.get_temp_data(city=city)
        return temp_data
    
    def process_data(self, city: str) -> WeatherData:
        weather_data = WeatherData.from_dict(data=self.get_temp_of_city(city=city))
        return weather_data
    
    def weather_of_city(self, city: str) -> str:
        weather_data: WeatherData = self.process_data(city=city)
        return f"The temp of {weather_data.location.name} is {weather_data.current.temp_c}C. It seems {weather_data.current.cloud}% cloudy day."
    
if __name__ == "__main__":
    city: str = input("Enter the city to get the weather info: ")
    app = App()
    print(app.weather_of_city(city=city))