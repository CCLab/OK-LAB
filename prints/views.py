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


def single(request, id):
    old_print = {
        'path': 'img/data/Acta et literae_0.jpg',
        'id': id,
        'title': "Lorem ipsum",
        'title_page': """ Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin ultrices, justo vel accumsan ultrices, est neque pellentesque metus, vitae congue diam libero in nunc. Vestibulum quis ex at arcu volutpat lacinia. Sed id orci in nisi congue condimentum. Maecenas egestas dolor ut metus congue congue. In faucibus risus ut consequat posuere. Nam lectus lacus, gravida a tempor non, vulputate non nisl. Donec arcu purus, molestie vel nibh vitae, viverra scelerisque arcu. Cras sed dignissim mi.\n\nMauris tempus eros sed felis egestas vulputate. Nullam laoreet efficitur bibendum. Morbi vitae facilisis felis. Pellentesque porta elementum urna eget venenatis. Aliquam tellus sapien, posuere a condimentum ut, mollis ac orci. Etiam fringilla hendrerit nisi, sed hendrerit turpis. Suspendisse mi sem, cursus eget nunc tincidunt, laoreet ultrices est. Praesent ex elit, iaculis nec turpis vitae, iaculis iaculis sapien. Duis felis dui, auctor sit amet lorem hendrerit, rhoncus facilisis arcu. Duis ut neque lorem. """,
        'date': '1562',
        'author': 'Lorem Ipsum Author',
        'place': 'Lorem Ipsum Place',
        'publisher': 'Lorem Ipsum Publisher',
        'signature': 's.4.34',
        'keywords': 'lorem ipsum dolor sit amet'.split(' ')
    }

    return render(request, "single.html", {'print': old_print})
