from django.db import models

class Ship(models.Model):
	imo = models.IntegerField()
	ship_name = models.CharField(default=None, max_length=100)

class Location(models.Model):
	ship = models.ForeignKey(Ship, on_delete=models.PROTECT)
	lat = models.FloatField(default=None)
	lng = models.FloatField(default=None)
	timestamp = models.DateTimeField(default=None)