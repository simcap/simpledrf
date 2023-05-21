import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cities.serializers import CitySerializer
from cities.models import City
from cities.services import LocalWeatherService, ServiceException

@api_view(['POST'])
def create_city(request):
    serializer = CitySerializer(data = request.data)
    if serializer.is_valid():
            service = LocalWeatherService(serializer.validated_data['lat'], serializer.validated_data['lon'])
            try:
                temperature = service.fetch_weather()
                serializer.save(temperature=temperature)
            except ServiceException as exception:
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