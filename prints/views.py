from django.shortcuts import render


def search(request):
    return render(request, "index.html")


def collection(request):
    paths = ["/img/data/Acta et literae_{}.jpg".format(i) for i in range(7)]
    return render(request, "filter_prints.html", {'paths': paths})


def by_name(request, letter=None):
    paths = ["/img/data/Acta et literae_{}.jpg".format(i) for i in range(7)]
    return render(request, "by_name.html", {'paths': paths})


def add(request):
    return search(request)


def filter(request):
    paths = ["/img/data/Acta et literae_{}.jpg".format(i) for i in range(7)]
    return render(request, "print_set.html", {'paths': paths})
