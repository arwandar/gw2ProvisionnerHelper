from api.models import ItemToken, Token


def getQtForItem(self, item):
    return ItemToken.objects.get(token=self, item=item).qt


Token.getQt = getQtForItem
