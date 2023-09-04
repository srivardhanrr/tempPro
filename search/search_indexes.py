from haystack import indexes
from .models import Place, College


class PlaceIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    location = indexes.LocationField(model_attr='location')
    address = indexes.CharField(model_attr='address')
    city = indexes.CharField(model_attr='city')

    def get_model(self):
        return Place

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class CollegeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    location = indexes.LocationField(model_attr='location')
    address = indexes.CharField(model_attr='address')
    city = indexes.CharField(model_attr='city')


    def get_model(self):
        return College

    def index_queryset(self, using=None):
        return self.get_model().objects.all()