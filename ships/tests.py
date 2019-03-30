from django.test import TestCase
from ships.models import Ship, Location
from rest_framework.test import APITestCase


class ShipTestCase(TestCase):
	def setUp(self):
		Ship.objects.create(ship_name="Mathilde Maersk​", imo="9632179")
		Ship.objects.create(ship_name="Australian Spirit", imo="9247455")
		Ship.objects.create(ship_name="MSC Preziosa", imo="9595321")
		# Create 3 Positions for first ship 9632179
		ship1 = Ship.objects.get(imo=9632179)
		Location.objects.create(ship=ship1,lat=51.8737335205078,lng=2.73133325576782,timestamp='2019-01-15 09:44:27+00')
		Location.objects.create(ship=ship1,lat=17.9850006103516,lng=-63.1359672546387,timestamp='2019-01-15 09:43:13+00')
		Location.objects.create(ship=ship1,lat=51.842098236084,lng=2.68831658363342,timestamp='2019-01-15 09:35:27+00')

	def test_ships_created(self):
		ships = Ship.objects.all()
		self.assertEqual(ships.count(), 3)

	def test_locations_created(self):
		locations = Location.objects.all()
		self.assertEqual(locations.count(), 3)

	def test_rest_api_get_all_ships(self):
		url = '/api/ships/'
		response = self.client.get(url, format='json')
		response_json = response.json()
		self.assertEqual(len(response_json), 3)
		self.assertEqual(response_json[0]['imo'], 9632179)
		self.assertEqual(response_json[1]['imo'], 9247455)
		self.assertEqual(response_json[2]['imo'], 9595321)

	def test_rest_api_get_ship_positions(self):
		url = '/api/positions/9632179/'
		response = self.client.get(url, format='json')
		response_json = response.json()
		self.assertEqual(len(response_json), 3)
		self.assertEqual(response_json[0]['lat'], 51.8737335205078)
		self.assertEqual(response_json[1]['lat'], 17.9850006103516)
		self.assertEqual(response_json[2]['lat'], 51.842098236084)



