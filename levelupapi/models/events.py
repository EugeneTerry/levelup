from django.db import models
from .gamers import Gamer
from .games import Games

class Events(models.Model):
  
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    game = models.ForeignKey(Games,
        on_delete=models.SET_DEFAULT, default=1)
    creator = models.ForeignKey(Gamer,
        on_delete=models.SET_DEFAULT, default=1)