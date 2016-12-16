import random

from django.shortcuts import render

LETTERS = [chr(i) for i in range(65, 91)]


def search(request):
    return render(request, "index.html")


def collection(request):
    paths = ["/img/data/Acta et literae_{}.jpg".format(i) for i in range(7)]
    return render(request, "filter_prints.html", {'paths': paths})


def by_name(request, letter=None):
    paths = ["/img/data/Acta et literae_{}.jpg".format(i) for i in range(7)]
    if letter:
        paths = [path for path in paths if random.choice([True, False])]
    return render(request, "by_name.html", {'paths': paths, 'letters': LETTERS})


def add(request):
    return search(request)


def filter(request):
    paths = ["/img/data/Acta et literae_{}.jpg".format(i) for i in range(7)]
    return render(request, "print_set.html", {'paths': paths})
