from api.models import CategoryToken, Category


def getQtForToken(self, token):
    return CategoryToken.objects.get(category=self, token=token).qt


Category.getQt = getQtForToken
