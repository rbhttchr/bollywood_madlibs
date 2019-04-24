from django.db import models
from django import forms
from django.forms import ModelForm
from .models import story000, story001

class form000(ModelForm):
    Bollywood_Actress_Name = models.CharField(max_length=128) # Name of Hindi Actress 1
    Bollywood_Actor_Name = models.CharField(max_length=128) # Name of Hindi Actor
    Body_Part_1 = models.CharField(max_length=128) # Body Part 1
    Body_Part_2 = models.CharField(max_length=128) # Body Part 2
    Old_Bollywood_Actor = models.CharField(max_length=128) # Old Hindi Actor
    Noun = models.CharField(max_length=128) # Noun
    Country = models.CharField(max_length=128) # Country
    Occupation_1 = models.CharField(max_length=128) # Occupation 1
    Past_Tense_Verb = models.CharField(max_length=128) # Past Tense Verb
    Occupation_2 = models.CharField(max_length=128) # Occupation 2
    Adjective_1 = models.CharField(max_length=128) # Adjective 1
    Adjective_2 = models.CharField(max_length=128) # Adjective 2
    Adjective_3 = models.CharField(max_length=128) # Adjective 3
    Number_between_1_and_10 = models.CharField(max_length=128) # Number between 1-10

    class Meta(ModelForm):
        model = story000
        fields = ('Bollywood_Actress_Name', 'Bollywood_Actor_Name',
                  'Body_Part_1', 'Body_Part_2', 'Old_Bollywood_Actor',
                  'Noun', 'Country', 'Occupation_1', 'Past_Tense_Verb',
                  'Occupation_2', 'Adjective_1', 'Adjective_2',
                  'Adjective_3', 'Number_between_1_and_10')

class form001(ModelForm):
    male_name = models.CharField(max_length=128, default='')
    present_participle = models.CharField(max_length=128, default='')
    adjective_1 = models.CharField(max_length=128, default='')
    girl_name = models.CharField(max_length=128, default='')
    movement = models.CharField(max_length=128, default='')
    number_1 = models.CharField(max_length=128, default='')
    adjective_2 = models.CharField(max_length=128, default='')
    number_2 = models.CharField(max_length=128, default='')
    location = models.CharField(max_length=128, default='')
    bollywood_actor = models.CharField(max_length=128, default='')
    bollywood_film = models.CharField(max_length=128, default='')
    adjective_3 = models.CharField(max_length=128, default='')

    class Meta(ModelForm):
        model = story001
        fields = ('male_name', 'present_participle', 'adjective_1', 'girl_name',
                  'movement', 'number_1', 'adjective_2', 'number_2',
                  'bollywood_actor', 'bollywood_film', 'adjective_3',)
