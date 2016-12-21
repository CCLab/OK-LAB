from django.shortcuts import render


def home(request):
    return render(request, 'search.html')


def static_site(template_name):
    return lambda request: render(request, template_name)
