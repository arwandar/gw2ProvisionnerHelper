from django.contrib import admin
from django.db import models

from api.utils import getPlop

from .Provisionner import Provisionner
from .Token import Token


# Create your models here.
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
        plop = ""
        tokens = self.tokens.all()
        for token in tokens:
            test = getPlop(self, token)
            print(test)
            plop = token
        return plop

    def tmp(self):
        return "plop"
