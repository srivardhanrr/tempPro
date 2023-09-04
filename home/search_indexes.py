from haystack import indexes
from .models import Home


class HomeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    address = indexes.CharField(model_attr='address')
    city = indexes.CharField(model_attr='city')
    location = indexes.LocationField(model_attr='location')

    def get_model(self):
        return Home

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
