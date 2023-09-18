from api.models import CategoryToken


def getBestToken(category):
    tokenRes = None
    for token in category.tokens.all():
        qt = CategoryToken.objects.get(
            category=category, token=token).qt
        if (tokenRes is None) or (qt < tokenRes.qt):
            tokenRes = {"qt": qt, "name": token.name}
    return "{qt} {name}".format(qt=tokenRes['qt'], name=tokenRes['name'])
