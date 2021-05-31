from django.db import models
from datetime import datetime
from django.utils.timezone import now

# Create your models here.
class Country(models.Model):
    country = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.country}'


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.name}'


class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Film(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(default= now)
    created_in_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    available_in_countries = models.ManyToManyField(Country, related_name='available_countries')
    category = models.ManyToManyField(Category)
    director = models.ForeignKey(Director,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

