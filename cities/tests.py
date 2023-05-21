from django.test import TestCase
from cities.models import City

class CitiesTestCase(TestCase):
    def setUp(self):
        City.objects.create(name="Paris", lat=48.86, lon=2.35)
        City.objects.create(name="Bogota", lat=4.37, lon=-74.06)

    def test_list_all_cities(self):
        cities = City.objects.all()
        self.assertTrue(len(cities) == 2)

