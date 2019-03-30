import csv

from ships.models import Ship
from ships.models import Location

with open('positions.csv') as csvfile:
	reader = csv.DictReader(csvfile,fieldnames=['imo','timestamp','lat','lng'])
	for row in reader:
		ship = Ship.objects.get(imo=row['imo'])
		p = Location(ship=ship, timestamp=row['timestamp'], lat=row['lat'], lng=row['lng'])
		p.save()