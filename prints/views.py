from django.shortcuts import render


def search(request):
    return render(request, "index.html")


def collection(request):
    paths = ["/img/data/Acta et literae_{}.jpg".format(i) for i in range(7)]
    return render(request, "collection.html", {'paths': paths})
