from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Place, College


@admin.register(Place)
class PlaceAdmin(OSMGeoAdmin):
    list_display = ('id', 'name', 'location', 'address', 'city')
    search_fields = ('name',)


@admin.register(College)
class CollegeAdmin(OSMGeoAdmin):
    list_display = ('id', 'name', 'location', 'address', 'city', 'state')
    search_fields = ('name',)
