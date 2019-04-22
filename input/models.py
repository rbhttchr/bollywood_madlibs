from django.db import models

# Create your models here.
class story(models.Model):
    Bollywood_Actress_Name = models.CharField(max_length=128, default='') # Name of Hindi Actress 1
    Bollywood_Actor_Name = models.CharField(max_length=128, default='') # Name of Hindi Actor
    Body_Part_1 = models.CharField(max_length=128, default='') # Body Part 1
    Body_Part_2 = models.CharField(max_length=128, default='') # Body Part 2
    Old_Bollywood_Actor = models.CharField(max_length=128, default='') # Old Hindi Actor
    Noun = models.CharField(max_length=128, default='') # Noun
    Country = models.CharField(max_length=128, default='') # Country
    Occupation_1 = models.CharField(max_length=128, default='') # Occupation 1
    Past_Tense_Verb = models.CharField(max_length=128, default='') # Past Tense Verb
    Occupation_2 = models.CharField(max_length=128, default='') # Occupation 2
    Adjective_1 = models.CharField(max_length=128, default='') # Adjective 1
    Adjective_2 = models.CharField(max_length=128, default='') # Adjective 2
    Adjective_3 = models.CharField(max_length=128, default='') # Adjective 3
    Number_between_1_and_10 = models.CharField(max_length=128, default='') # Number between 1-10


    def __str__(self):
        return str(self.id) + " " + self.Bollywood_Actress_Name
