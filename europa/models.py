from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    surface = models.FloatField()
    population = models.IntegerField()
    description = models.TextField()
    image_url = models.CharField(max_length=2038)


class Dishes(models.Model):
    name = models.CharField(max_length=255)
    ingredients_number = models.IntegerField()
    quantity = models.IntegerField()
    preparation_time = models.FloatField()
    description = models.TextField()
    image_url = models.CharField(max_length=2038)
    dish_country = models.CharField(max_length=255, default='None')
