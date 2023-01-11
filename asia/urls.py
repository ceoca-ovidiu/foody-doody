from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('russia/', views.russia, name='russia'),
    path('china/', views.china, name='china'),
    path('japan/', views.japan, name='japan'),
    path('india/', views.india, name='india'),
    path('turkey/', views.turkey, name='turkey'),
    path('saudiarabia/', views.saudiarabia, name='saudiarabia'),
]