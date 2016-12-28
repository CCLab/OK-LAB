import json
import random

from django.conf import settings
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from prints.models import OldPrint

LETTERS = [chr(i) for i in range(65, 91)]


def search(request):
    return render(request, "search.html")


def filter(request=None, page=1, filter=None, order=None):
    try:
        queryset = OldPrint.objects
        if filter:
            queryset = filter.apply(queryset)
        else:
            queryset = queryset.all()
        if order:
            queryset = queryset.order_by(order)
        paginator = Paginator(queryset, settings.PRINTS_PER_PAGE)

        prints = [old_print.dict for old_print in paginator.page(page)]
    except:
        prints = []
    # paths = ["/img/data/Acta et literae_{}.jpg".format(i) for i in range(7)]
    # paths = [path for path in paths if random.choice([True, False])]
    # return render(request, "print_set.html", {'prints': paths})
    if request:
        print(request.GET)
        return HttpResponse(json.dumps(prints))
    json.dumps(prints)


def collection(request):
    prints = filter(page=1)
    return render(request, "collection.html", {'prints': prints,
                                                  'letters': LETTERS,
                                                  'default_title_page': settings.DEFAULT_TITLE_PAGE})


def by_name(request, letter=None):
    paths = ["/img/data/Acta et literae_{}.jpg".format(i) for i in range(7)]
    # if letter:
    #     paths = [path for path in paths if random.choice([True, False])]
    return render(request, "by_name.html",
                  {'prints': {letter: [random.choice(paths)] * random.randint(2, 5) for letter in LETTERS},
                   'letters': LETTERS})


def single(request, id):
    return render(request, "single.html", {'print': get_object_or_404(OldPrint, id=id),
                                           'default_title_page': settings.DEFAULT_TITLE_PAGE})


def view(request, id):
    return render(request, "single.html", {'print': get_object_or_404(OldPrint, id=id)})

