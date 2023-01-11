from django.shortcuts import render
from django.http import HttpResponse
from .models import Country, Dishes


def home(request):
    countries = Country.objects.all()
    return render(request, 'america.html', {'countries': countries})


def unitedstates(request):
    country_name = 'United States'
    dishes = Dishes.objects.all()
    return render(request, 'unitedstates.html', {'country_name': country_name,
                                                 'dishes': dishes})


def brazil(request):
    country_name = 'Brazil'
    dishes = Dishes.objects.all()
    return render(request, 'brazil.html', {'country_name': country_name,
                                           'dishes': dishes})


def mexico(request):
    country_name = 'Mexico'
    dishes = Dishes.objects.all()
    return render(request, 'mexico.html', {'country_name': country_name,
                                           'dishes': dishes})


def canada(request):
    return render(request, 'canada.html')


def cuba(request):
    return render(request, 'cuba.html')


def argentina(request):
    return render(request, 'argentina.html')
