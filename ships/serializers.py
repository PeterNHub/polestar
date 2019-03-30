from rest_framework import serializers
from ships.models import Location, Ship


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('lat','lng','timestamp')

class ShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ship
        fields = ('imo','ship_name')