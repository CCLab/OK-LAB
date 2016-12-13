from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def static_site(template_name):
    return lambda request: render(request, template_name)
