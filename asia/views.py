from django.shortcuts import render
from django.http import HttpResponse
from .models import Country, Dishes


def home(request):
    countries = Country.objects.all()
    return render(request, 'asia.html', {'countries': countries})


def russia(request):
    country_name = 'Russia'
    dishes = Dishes.objects.all()
    return render(request, 'russia.html', {'country_name': country_name,
                                           'dishes': dishes})


def china(request):
    country_name = 'China'
    dishes = Dishes.objects.all()
    return render(request, 'china.html', {'country_name': country_name,
                                          'dishes': dishes})


def japan(request):
    return render(request, 'japan.html')


def india(request):
    country_name = 'India'
    dishes = Dishes.objects.all()
    return render(request, 'india.html', {'country_name': country_name,
                                          'dishes': dishes})


def turkey(request):
    return render(request, 'turkey.html')


def saudiarabia(request):
    return render(request, 'saudiarabia.html')
