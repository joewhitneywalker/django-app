from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

GENDER_CHOICES = (
("F", "Female"), 
("M", "Male"),
("X", "Fluid")
)


class CharacterPowers(models.Model):
    characterpowers = models.CharField(max_length=100) #name in cattoy reference
    
    def __str__(self):
        return self.characterpowers #self.name?



class Character(models.Model):
    name = models.CharField(max_length=20)
    img = models.CharField(max_length=500)
    age = models.IntegerField()
    attribute = models.CharField(max_length=500)
    gender = models.CharField(max_length=10, choices = GENDER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    characterpowers = models.ManyToManyField(CharacterPowers)#has to be lower case to add a character, has to be camel case to render character detail
    

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

