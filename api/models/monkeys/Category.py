from api.models import CategoryToken, Category


def getQtForToken(self, token):
    return CategoryToken.objects.get(category=self, token=token).qt


Category.getQt = getQtForToken


def getBestToken(self):
    tokenRes = None
    for token in self.tokens.all():
        qt = self.getQt(token)
        if (tokenRes is None) or (qt < tokenRes.qt):
            tokenRes = {"qt": qt, "name": token.name}
    return "{qt} {name}".format(qt=tokenRes["qt"], name=tokenRes["name"])


Category.getBestToken = getBestToken
