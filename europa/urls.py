from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('romania/', views.romania, name='romania'),
    path('france/', views.france, name='france'),
    path('spain/', views.spain, name='spain'),
    path('italy/', views.italy, name='italy'),
    path('germany/', views.germany, name='germany'),
    path('greece/', views.greece, name='greece'),
]
