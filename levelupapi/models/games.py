from django.db import models
from .gamers import Gamer
from .types import Type

class Games(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(Type,
        on_delete=models.SET_DEFAULT, default=1)
    game_creator = models.ForeignKey(Gamer,
        on_delete=models.SET_DEFAULT, default=1)
    