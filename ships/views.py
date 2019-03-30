from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse

from rest_framework import viewsets, generics

import json
from ships.models import Ship, Location
from ships.serializers import LocationSerializer,ShipSerializer

class ShipList(generics.ListAPIView):
   serializer_class = ShipSerializer

   def get_queryset(self):
       return Ship.objects.all()

class LocationList(generics.ListAPIView):
   serializer_class = LocationSerializer

   def get_queryset(self):
       imo = self.kwargs['ship']
       ship = Ship.objects.get(imo=imo)
       return Location.objects.filter(ship=ship).order_by('-timestamp')


# @api_view(["GET"])
# def ShipsList(params):
#     try:
#     	ships = Ship.objects.all()
#     	ships_list = []
#     	for ship in ships:
#     		ships_list.append({"imo":ship.imo,"name":ship.ship_name})
#     	# ships_list = list(ships)
#     	return JsonResponse(ships_list, safe=False)
#     	# data = serializers.serialize('json', ships_list)
#     	# return HttpResponse(data, content_type="application/json")
#     except ValueError as e:
#         return Response(e.args[0],status.HTTP_400_BAD_REQUEST)