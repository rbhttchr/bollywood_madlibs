from django.db import models

# Create your models here.
class story000(models.Model):
    bollywood_actress_name = models.CharField(max_length=128, default='') # Name of Hindi Actress 1
    bollywood_actor_name = models.CharField(max_length=128, default='') # Name of Hindi Actor
    body_part_1 = models.CharField(max_length=128, default='') # Body Part 1
    body_part_2 = models.CharField(max_length=128, default='') # Body Part 2
    old_Bollywood_actor = models.CharField(max_length=128, default='') # Old Hindi Actor
    noun = models.CharField(max_length=128, default='') # Noun
    country = models.CharField(max_length=128, default='') # Country
    occupation_1 = models.CharField(max_length=128, default='') # Occupation 1
    past_tense_verb = models.CharField(max_length=128, default='') # Past Tense Verb
    occupation_2 = models.CharField(max_length=128, default='') # Occupation 2
    adjective_1 = models.CharField(max_length=128, default='') # Adjective 1
    adjective_2 = models.CharField(max_length=128, default='') # Adjective 2
    adjective_3 = models.CharField(max_length=128, default='') # Adjective 3
    number_between_1_and_10 = models.CharField(max_length=128, default='') # Number between 1-10


    def __str__(self):
        return str(self.id) + " " + self.Bollywood_Actress_Name

class story001(models.Model):
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

    def __str__(self):
        return str(self.id) + " " + self.male_name

class story002(models.Model):
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

    def __str__(self):
        return str(self.id) + " " + self.male_name_1

class story003(models.Model):
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

    def __str__(self):
        return str(self.id) + " " + self.girl_name
