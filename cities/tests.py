from django.test import TestCase
from unittest.mock import patch
from rest_framework import status
from rest_framework.test import APITestCase
from cities.models import City
from cities.services import LocalWeatherService

class CitiesTestCase(TestCase):
    def setUp(self):
        City.objects.create(name="Paris", lat=48.86, lon=2.35)
        City.objects.create(name="Bogota", lat=4.37, lon=-74.06)

    def test_list_all_cities(self):
        cities = City.objects.all()
        self.assertTrue(len(cities) == 2)


class CitiesWithTemperature(APITestCase):
    def test_create_city_and_temperature(self):
        with patch.object(LocalWeatherService, 'fetch_weather', return_value=28.4):
            response = self.client.post('/cities/new', {'name': 'London', 'lon': 76, 'lat': 0 })
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            city = City.objects.filter(name = 'London').first()
            self.assertEqual(city.temperature, 28.4)
