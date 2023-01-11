from django.shortcuts import render
from django.http import HttpResponse
from .models import Dishes


def home(request):
    country_name = 'Australia'
    dishes = Dishes.objects.all()
    return render(request, 'australia.html', {'country_name': country_name,
                                              'dishes': dishes})
