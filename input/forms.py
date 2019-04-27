from django.db import models
from django import forms
from django.forms import ModelForm
from .models import story000, story001, story002, story003

class form000(ModelForm):
    bollywood_actress_name = models.CharField(max_length=128) # Name of Hindi Actress 1
    bollywood_actor_name = models.CharField(max_length=128) # Name of Hindi Actor
    body_part_1 = models.CharField(max_length=128) # Body Part 1
    body_part_2 = models.CharField(max_length=128) # Body Part 2
    old_Bollywood_actor = models.CharField(max_length=128) # Old Hindi Actor
    noun = models.CharField(max_length=128) # Noun
    country = models.CharField(max_length=128) # Country
    occupation_1 = models.CharField(max_length=128) # Occupation 1
    past_tense_verb = models.CharField(max_length=128) # Past Tense Verb
    occupation_2 = models.CharField(max_length=128) # Occupation 2
    adjective_1 = models.CharField(max_length=128) # Adjective 1
    adjective_2 = models.CharField(max_length=128) # Adjective 2
    adjective_3 = models.CharField(max_length=128) # Adjective 3
    number_between_1_and_10 = models.CharField(max_length=128) # Number between 1-10

    class Meta(ModelForm):
        model = story000
        fields = ('bollywood_actress_name', 'bollywood_actor_name',
                  'body_part_1', 'body_part_2', 'old_Bollywood_actor',
                  'noun', 'country', 'occupation_1', 'past_tense_verb',
                  'occupation_2', 'adjective_1', 'adjective_2',
                  'adjective_3', 'number_between_1_and_10')

class form001(ModelForm):
    male_name = models.CharField(max_length=128, default='')
    action_word = models.CharField(max_length=128, default='')
    adjective_1 = models.CharField(max_length=128, default='')
    girl_name = models.CharField(max_length=128, default='')
    movement = models.CharField(max_length=128, default='')
    number_1 = models.CharField(max_length=128, default='')
    location = models.CharField(max_length=128, default='')
    adjective_2 = models.CharField(max_length=128, default='')
    number_2 = models.CharField(max_length=128, default='')
    bollywood_actor_name = models.CharField(max_length=128, default='')
    bollywood_film = models.CharField(max_length=128, default='')
    adjective_3 = models.CharField(max_length=128, default='')

    class Meta(ModelForm):
        model = story001
        fields = ('male_name', 'action_word', 'adjective_1', 'girl_name',
                  'movement', 'number_1', 'location', 'adjective_2',
                  'number_2', 'bollywood_actor_name', 'bollywood_film', 'adjective_3',)

class form002(ModelForm):
    male_name_1 = models.CharField(max_length=128, default='')
    male_name_2 = models.CharField(max_length=128, default='')
    male_name_3 = models.CharField(max_length=128, default='')
    girl_name = models.CharField(max_length=128, default='')
    number = models.CharField(max_length=128, default='')
    relative_1 = models.CharField(max_length=128, default='')
    relative_2 = models.CharField(max_length=128, default='')
    animal_1 = models.CharField(max_length=128, default='')
    mode_of_transportation = models.CharField(max_length=128, default='')
    city = models.CharField(max_length=128, default='')
    noun_1 = models.CharField(max_length=128, default='')
    noun_2 = models.CharField(max_length=128, default='')
    slogan = models.CharField(max_length=512, default='')
    past_tense_verb_1 = models.CharField(max_length=128, default='')
    past_tense_verb_2 = models.CharField(max_length=128, default='')
    animal_2 = models.CharField(max_length=128, default='')
    animal_3 = models.CharField(max_length=128, default='')

    class Meta(ModelForm):
        model = story002
        fields = ('male_name_1', 'male_name_2', 'male_name_3', 'girl_name',
                  'number', 'relative_1', 'relative_2', 'animal_1',
                  'mode_of_transportation', 'city', 'noun_1',
                  'noun_2', 'slogan', 'past_tense_verb_1', 'past_tense_verb_2',
                  'animal_2', 'animal_3',)

class form003(ModelForm):
    adjective_1 = models.CharField(max_length=128, default='')
    color = models.CharField(max_length=128, default='')
    type_of_relative = models.CharField(max_length=128, default='')
    adjective_2 = models.CharField(max_length=128, default='')
    adjective_3 = models.CharField(max_length=128, default='')
    city = models.CharField(max_length=128, default='')
    adjective_4 = models.CharField(max_length=128, default='')
    girl_name = models.CharField(max_length=128, default='')
    noun = models.CharField(max_length=128, default='')
    illness = models.CharField(max_length=128, default='')
    adjective_5 = models.CharField(max_length=128, default='')
    adjective_6 = models.CharField(max_length=128, default='')
    adjective_7 = models.CharField(max_length=128, default='')

    class Meta(ModelForm):
        model = story003
        fields = ('adjective_1', 'color', 'type_of_relative', 'adjective_2',
                  'adjective_3', 'city', 'adjective_4', 'girl_name', 'noun',
                  'illness', 'adjective_5', 'adjective_6', 'adjective_7',)
