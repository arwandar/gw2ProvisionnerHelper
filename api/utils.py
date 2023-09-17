from api.models import CategoryToken


def getPlop(category, token):
    return CategoryToken.objects.get(category=category, token=token)
