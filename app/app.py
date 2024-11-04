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
        try:
            temp_data: Dict[str, Any] = self._request_api.get_temp_data(city=city)
            return temp_data
        except Exception as error:
            self._logging.exception(f"May be invalid input data.{error}")
            return None
    
    def process_data(self, city: str) -> WeatherData:
        try:
            data: WeatherData = self.get_temp_of_city(city=city)
            if data:
                weather_data: WeatherData = WeatherData.from_dict(data=self.get_temp_of_city(city=city))
                return weather_data
            else:
                return None
        except Exception as error:
            self._logging.exception(f"There is problem processing the data. {error}")
            return None

    def weather_of_city(self, city: str) -> str:
        try:
            data = self.process_data(city=city)
            if data:
                weather_data: WeatherData = self.process_data(city=city)
                return f"The temp of {weather_data.location.name} is {weather_data.current.temp_c}C. It seems {weather_data.current.cloud}% cloudy day."
            else:
                self._logging.warning(f"No data to Process.")
                return None
        except Exception as error:
            self._logging.exception(f"There is problem gathering the data.{error}")
            return None
    
if __name__ == "__main__":
    city: str = input("Enter the city to get the weather info: ")
    app = App()
    print(app.weather_of_city(city=city))