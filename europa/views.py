from django.shortcuts import render

from .models import Country, Dishes


def home(request):
    countries = Country.objects.all()
    return render(request, 'europa.html', {'countries': countries})


def romania(request):
    country_name = 'Romania'
    dishes = Dishes.objects.all()
    return render(request, 'romania.html', {'country_name': country_name,
                                            'dishes': dishes})


def france(request):
    country_name = 'France'
    dishes = Dishes.objects.all()
    return render(request, 'france.html', {'country_name': country_name,
                                           'dishes': dishes})


def spain(request):
    country_name = 'Spain'
    dishes = Dishes.objects.all()
    return render(request, 'spain.html', {'country_name': country_name,
                                          'dishes': dishes})


def italy(request):
    country_name = 'Italy'
    dishes = Dishes.objects.all()
    return render(request, 'italy.html', {'country_name': country_name,
                                          'dishes': dishes})


def germany(request):
    country_name = 'Germany'
    dishes = Dishes.objects.all()
    return render(request, 'germany.html', {'country_name': country_name,
                                            'dishes': dishes})


def greece(request):
    country_name = 'Greece'
    dishes = Dishes.objects.all()
    return render(request, 'greece.html', {'country_name': country_name,
                                           'dishes': dishes})
