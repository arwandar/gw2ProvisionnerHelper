from django.contrib import admin

from .models import Category, CategoryToken, Item, ItemToken, Provisionner, Token

# Register your models here.
admin.site.register(Category)
admin.site.register(CategoryToken)
admin.site.register(Item)
admin.site.register(ItemToken)
admin.site.register(Provisionner)
admin.site.register(Token)
