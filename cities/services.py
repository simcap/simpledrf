import json
from urllib.error import HTTPError
from urllib.request import urlopen

class LocalWeatherService:

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def fetch_weather(self):
        url = f"https://api.open-meteo.com/v1/meteofrance?latitude={self.lat}&longitude={self.lon}&current_weather=true"
        
        try:
            with urlopen(url) as response:
                body = response.read()
                data = json.loads(body.decode('utf-8'))
                if "error" in data:
                    raise ServiceException(data['reason'])
                return data['current_weather']['temperature']
        except HTTPError as err:
            raise ServiceException(err) 

class ServiceException(Exception):
    """Used when third party service returns an error"""
