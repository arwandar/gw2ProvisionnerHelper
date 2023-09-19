from django.db import models

from .Category import Category
from .Token import Token


class CategoryToken(models.Model):
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    qt = models.IntegerField()

    def __str__(self):
        return "{provisionner}: {qt} {token}".format(
            provisionner=self.category.provisionner.name,
            qt=self.qt,
            token=self.token.name,
        )
