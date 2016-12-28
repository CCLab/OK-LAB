from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from management.forms import OldPrintForm
from prints.models import OldPrint


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
