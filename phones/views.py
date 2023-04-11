from django.shortcuts import render, redirect
from phones.management.commands.import_phones import handle


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_by = request.GET.get('name', 'min_price', 'max_price')
    if sort_by == 'name':
        phones = phones.order_by('name')
    elif sort_by == 'min_price':
        phones = phones.order_by('price')
    elif sort_by == 'max_price':
        phones = phones.order_by('-price')
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phones': phones}
    return render(request, template, context)
