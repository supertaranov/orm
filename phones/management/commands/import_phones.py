import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.shortcuts import render
from django.core.paginator import Paginator


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            phones_data = (
                phone['name'],
                phone['image'], 
                phone['price'],
                phone['release_date'],
                phone['lte_exists'],
            )
        sort_by = request.GET.get('name', 'min_price', 'max_price')
        if sort_by == 'name':
           phones = phones.order_by('name')
        elif sort_by == 'min_price':
           phones = phones.order_by('price')
        elif sort_by == 'max_price':
            phones = phones.order_by('-price')
        paginator = Paginator(phones, 3)
        sort = paginator.get_page(sort_by)
        context = {
                'sort': sort,
                'phones': phones_data,
        }    
        return render(request, 'templates/catalog.html', context)