from django.db import models
from .gamers import Gamer
from .gametypes import GameType

class Games(models.Model):
    name = models.CharField(max_length=50)
    gametype = models.ForeignKey(GameType,
        on_delete=models.SET_DEFAULT, default=1)
    game_creator = models.ForeignKey(Gamer,
        on_delete=models.SET_DEFAULT, default=1)
    