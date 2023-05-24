import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cities.serializers import CitySerializer
from cities.models import City
from cities.services import LocalTemperatureService, ServiceException

@api_view(['POST'])
def create_city(request):
    serializer = CitySerializer(data = request.data)
    if serializer.is_valid():
            service = LocalTemperatureService(serializer.validated_data['name'], serializer.validated_data['lat'], serializer.validated_data['lon'])
            try:
                temp = service.fetch_temperature()
                serializer.save(temperature=temp)
            except ServiceException as e:
                return Response({'error': f"weather services responded: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
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