from django.shortcuts import render
from haystack.query import SearchQuerySet
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.contrib.gis.db.models.functions import Distance
from .models import Home
from search.models import Place, College


longitude = 77.607436
latitude = 12.934504

user_location = Point(longitude, latitude, srid=4326)


class HomeView(generic.ListView):
    model = Home
    context_object_name = 'shops'
    queryset = Home.objects.annotate(distance=Distance('location', user_location)).order_by('distance')[0:3]
    template_name = 'home/index.html'

    def get(self, request, **kwargs):
        # Return shops ordered by distance to user
        result = SearchQuerySet().models(College, Place, Home).dwithin('location', user_location, D(mi=10)).distance('location',
                                                                                                                         user_location).order_by(
            'distance')
        context = {"result": result}
        return render(request, template_name=self.template_name, context=context)

