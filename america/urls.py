from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('unitedstates/', views.unitedstates, name='unitedstates'),
    path('brazil/', views.brazil, name='brazil'),
    path('mexico/', views.mexico, name='mexico'),
    path('canada/', views.canada, name='canada'),
    path('cuba/', views.cuba, name='cuba'),
    path('argentina/', views.argentina, name='argentina'),
]