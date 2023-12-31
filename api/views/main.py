from django.shortcuts import render

from api.models import Category


class Line:
    def __init__(self, category):
        self.provisionner = category.provisionner
        self.token = category.getBestToken()


def props(cls):
    return [i for i in cls.__dict__.keys() if i[:1] != "_"]


def main(request):
    categories = Category.objects.all().prefetch_related("tokens")
    lines = []
    for category in categories:
        lines.append(Line(category))

    return render(
        request,
        template_name="main.html",
        context={
            "lines": lines,
        },
    )
