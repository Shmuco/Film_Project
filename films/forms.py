from django import forms
from .models import *


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        # fields = ['title',
        #             'release_date',
        #             'created_in_country',
        #             'available_in_countries',
        #             'category',
        #             'director']
        exclude = []


class FilmForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
        