import json
from rest_framework import status
from urllib.error import HTTPError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from urllib.request import urlopen
from cities.serializers import CitySerializer
from cities.models import City

@api_view(['POST'])
def create_city(request):
    serializer = CitySerializer(data = request.data)
    if serializer.is_valid():
            try:
                temperature = fetch_temperature_from_lon_lat(serializer.validated_data['lat'], serializer.validated_data['lon'])
                serializer.save(temperature=temperature)
            except FetchTemperatureException as exception:
                return Response({'error': f"weather service responded: {str(exception)}"})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_cities(request):
    """
    List all cities, with temperatures that were added on city creation.
    """
    cities = City.objects.all()
    serializer = CitySerializer(cities, many=True)
    return Response(serializer.data)

def fetch_temperature_from_lon_lat(lon, lat):
    url = f"https://api.open-meteo.com/v1/meteofrance?latitude={lat}&longitude={lon}&current_weather=true"
    try:
        with urlopen(url) as response:
            body = response.read()
            data = json.loads(body.decode('utf-8'))
            if "error" in data:
                raise FetchTemperatureException(data['reason'])
        
            return data['current_weather']['temperature']
    except HTTPError as err:
        raise FetchTemperatureException(err) 

class FetchTemperatureException(Exception):
    """Used when weather API returns an error"""
