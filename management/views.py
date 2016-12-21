from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def manage(request):
    return render(request, 'search.html')


@login_required
def add(request):
    return render(request, 'search.html')


@login_required
def edit(request, id):
    return render(request, 'search.html')


@login_required
def remove(request, id):
    return render(request, 'search.html')
