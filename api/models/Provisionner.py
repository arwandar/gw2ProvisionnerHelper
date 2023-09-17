from django.contrib import admin
from django.db import models


class Provisionner(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    locationCode = models.CharField(max_length=100)

    def __str__(self):
        return "{name}: {location} {locationCode}".format(
            name=self.name, location=self.location, locationCode=self.locationCode
        )
