from django.shortcuts import render, redirect
from phones.management.commands.import_phones import phones_data


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = {'phones': phones_data}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phones': phones_data}
    return render(request, template, context)
