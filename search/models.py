from django.contrib.gis.db import models


class Place(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class College(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100, default="Bengaluru")
    state = models.CharField(max_length=100, default="Karnataka")

    def __str__(self):
        return self.name
