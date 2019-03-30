from django.contrib import admin

from ships.models import Ship
from ships.models import Location

admin.site.register(Ship)
admin.site.register(Location)