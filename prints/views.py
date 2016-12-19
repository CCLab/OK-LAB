import json
import random

from django.shortcuts import render

LETTERS = [chr(i) for i in range(65, 91)]


def search(request):
    return render(request, "index.html")


def collection(request):
    prints = [{'id': i, 'path': "img/data/Acta et literae_{}.jpg".format(i), 'idex': random.choice(LETTERS)} for i in range(7)]
    return render(request, "filter_prints.html", {'prints': json.dumps(prints), 'letters': LETTERS})


def by_name(request, letter=None):
    paths = ["/img/data/Acta et literae_{}.jpg".format(i) for i in range(7)]
    # if letter:
    #     paths = [path for path in paths if random.choice([True, False])]
    return render(request, "by_name.html", {'prints': {letter: [random.choice(paths)]*random.randint(2, 5) for letter in LETTERS}, 'letters': LETTERS})


def add(request):
    return search(request)


def filter(request):
    paths = ["/img/data/Acta et literae_{}.jpg".format(i) for i in range(7)]
    paths = [path for path in paths if random.choice([True, False])]
    return render(request, "print_set.html", {'prints': paths})
