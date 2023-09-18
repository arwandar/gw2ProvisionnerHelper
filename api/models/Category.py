from django.contrib import admin
from django.db import models

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
