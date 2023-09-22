from typing import Any
from django.contrib import admin
from django.db import models
import requests

from api.utils import formatPrice


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    apiId = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def getPrice(self):
        url = "https://api.guildwars2.com/v2/commerce/prices/{id}".format(id=self.apiId)
        res = requests.get(url).json()
        buyPrice = res["buys"]["unit_price"]
        return buyPrice
