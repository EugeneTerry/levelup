from django.db import models
from gamers import Gamer

class Events(models.Model):
  
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    game = models.CharField(max_length=50)
    event_creator = models.OneToOneField(Gamer, on_delete=models.CASCADE)