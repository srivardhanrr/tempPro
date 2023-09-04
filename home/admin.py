from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Home


@admin.register(Home)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')
