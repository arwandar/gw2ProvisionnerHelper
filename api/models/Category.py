from django.contrib import admin
from django.db import models

from api.utils import formatPrice

from .Provisionner import Provisionner
from .Token import Token


class Category(models.Model):
    categoryId = models.AutoField(primary_key=True)
    maxPerDay = models.IntegerField()
    provisionner = models.ForeignKey(Provisionner, on_delete=models.CASCADE)
    tokens = models.ManyToManyField(Token, through="CategoryToken")

    def __str__(self):
        return "{provisionner} {categoryId}".format(
            provisionner=self.provisionner.name, categoryId=self.categoryId
        )

    def getBestToken(self):
        tokenRes = None
        for token in self.tokens.all():
            qt = self.getQt(token)
            price = token.getValue()
            if (tokenRes is None) or (qt * price < tokenRes["qt"] * tokenRes["price"]):
                tokenRes = {"qt": qt, "name": token.name, "price": price}
        return "{qt} {name}({price})".format(
            qt=tokenRes["qt"],
            name=tokenRes["name"],
            price=formatPrice(tokenRes["price"]),
        )
