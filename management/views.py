from django.shortcuts import render


def manage(request):
    return render(request, 'search.html')


def add(request, id):
    return render(request, 'search.html')


def edit(request, id):
    return render(request, 'search.html')


def remove(request, id):
    return render(request, 'search.html')
