from django.db import models
from .gamers import Gamer

class Games(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    # game_creator = models.OneToOneField(Gamer, on_delete=models.CASCADE())
    