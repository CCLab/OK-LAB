from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from management.forms import OldPrintForm
from prints.models import OldPrint, Scan
import os


@login_required
def manage(request):
    return render(request, 'search.html')


@login_required
def remove(request, id):
    return render(request, 'search.html')


@login_required
def edit(request, id):
    old_print = get_object_or_404(OldPrint, id=id)
    if request.method == 'POST':
        form = OldPrintForm(request.POST, instance=old_print)
        if form.is_valid():
            form.save()
            return redirect('prints:single', old_print.id)
    else:
        form = OldPrintForm(instance=old_print)

    return render(request, 'form.html', {'form': form, 'title': 'Edycja'})


@login_required
def add(request):
    if request.method == 'POST':
        form = OldPrintForm(request.POST)
        if form.is_valid():
            old_print = form.save(commit=False)
            old_print.owner = request.user
            old_print.save()
            return redirect('prints:single', old_print.id)
    else:
        form = OldPrintForm()

    return render(request, 'form.html', {'form': form, 'title': 'Nowy druk'})


def handle_uploaded_file(f, path):
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@login_required
def upload_title_page(request, id):
    if request.method == 'POST':
        old_print = get_object_or_404(OldPrint, id=id)
        scan = Scan()
        scan.page_number = 0
        scan.format = str(request.FILES['file']).split('.')[-1]
        scan.old_print = old_print
        scan.save()
        old_print.title_page = scan
        old_print.save()
        if not os.path.exists(old_print.path):
            os.makedirs(old_print.path)
        if os.path.exists(scan.path):
            os.remove(scan.path)
        handle_uploaded_file(request.FILES['file'], scan.path)
        return HttpResponse(str(scan.static))
    return HttpResponseBadRequest("ERROR")
