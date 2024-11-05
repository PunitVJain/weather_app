from typing import Dict, Any
import requests
import os
from dotenv import load_dotenv
import logging

load_dotenv()


class RequestApi(object):

    def __init__(self) -> None:
        self._logging = logging.getLogger(self.__class__.__name__)

    def get_temp_data(self, city: str) -> Dict[str, Any]:
        try:
            
            data = requests.get(url=os.getenv("URL"), params={"key": os.getenv("API_KEY"), "q": city})
            if data.status_code == 200:
                self._logging.info(f"Api is working with {data.status_code}")
                return data.json()
            else:
                self._logging.error(f"The weather api is not working, may be invalid input {data.status_code}")
                return None
        except (Exception, TimeoutError) as error:
            self._logging.exception(f"Exception raised {error}")
            return None