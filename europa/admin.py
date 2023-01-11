from django.contrib import admin

from .models import Country, Dishes


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'surface', 'population', 'description', 'image_url')


class DishesAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'ingredients_number', 'quantity', 'preparation_time', 'description', 'image_url', 'dish_country')


admin.site.register(Country, CountryAdmin)
admin.site.register(Dishes, DishesAdmin)
