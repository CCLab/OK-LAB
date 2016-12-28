import json
import random

from django.conf import settings
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from prints.filters import PrintsFilter
from prints.models import OldPrint

LETTERS = [chr(i) for i in range(65, 91)]


def search(request):
    return render(request, "search.html")


def filter(request, page=1):
    filter = PrintsFilter(request.GET)
    filter.queryset.order_by('title')

    paginator = Paginator(filter.qs.order_by('title'), settings.PRINTS_PER_PAGE)

    prints = [old_print.dict for old_print in paginator.page(page)]
    return HttpResponse(json.dumps(prints))


def collection(request):
    paginator = Paginator(OldPrint.objects.all(), settings.PRINTS_PER_PAGE)
    prints = [old_print.dict for old_print in paginator.page(1)]
    return render(request, "collection.html", {'prints': json.dumps(prints),
                                               'letters': LETTERS,
                                               'default_title_page': settings.DEFAULT_TITLE_PAGE,
                                               'filter': PrintsFilter()})


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
