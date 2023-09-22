from django.contrib import admin
from django.db import models

from .Item import Item


def props(cls):
    return [i for i in cls.__dict__.keys() if i[:1] != "_"]


class Token(models.Model):
    name = models.CharField(max_length=100)
    items = models.ManyToManyField(Item, through="ItemToken")

    def __str__(self):
        return self.name

    def getValue(self):
        sum = 0
        for item in self.items.all():
            qt = self.getQt(item)
            price = item.getPrice()
            sum += qt * price

        return sum
