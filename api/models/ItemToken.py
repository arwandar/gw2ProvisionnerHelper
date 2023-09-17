from django.contrib import admin
from django.db import models

from .Item import Item
from .Token import Token


class ItemToken(models.Model):
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    qt = models.IntegerField()

    def __str__(self):
        return "{token}: {qt} {item}".format(
            token=self.token.name, qt=self.qt, item=self.item.name
        )
