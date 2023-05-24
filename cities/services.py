import json
from urllib.error import HTTPError
import requests

class LocalTemperatureService:

    def __init__(self, city_name, lat, lon):
        self.city = city_name
        self.lat = lat
        self.lon = lon

    def fetch_temperature(self):
        temperature, failed_msg = self._with_world_weather()
        if failed_msg:
            temperature, err_msg = self._with_open_meteo()
            if err_msg:
                raise ServiceException(f"all weather services failed: {failed_msg}, {err_msg}")
            return temperature
        return temperature

    def _with_open_meteo(self):
        url = f"https://api.open-meteo.com/v1/meteofrance?latitude={self.lat}&longitude={self.lon}&current_weather=true"
        
        try:
            body = requests.get(url).json()
            if 'error' in body:
                return 0, body['reason']
            return body['current_weather']['temperature'], ""
        except requests.exceptions.RequestException as err:
            return 0, str(err)

    def _with_world_weather(self):
        """
        On purpose this will always fail (as we do not provide an API key)
        """
        url = f"https://api.worldweatheronline.com/premium/v1/weather.ashx?format=json&q={self.city}" 
        try:
            resp = requests.get(url)
            if resp.status_code not in (200, 201,):
                return 0, f"error: world weather online return {resp.status_code}"
            else:
                return 0, "" # here we do not care, will never happen
        except requests.exceptions.RequestException as err:
            return 0, str(err) 

class ServiceException(Exception):
    """Service returned an error"""
