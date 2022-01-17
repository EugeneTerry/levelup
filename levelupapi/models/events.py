from django.db import models


from .gamers import Gamer
from .games import Games
from levelupapi.models import eventstatus

class Events(models.Model):
  
    title = models.CharField(max_length=50, default = "Unnamed Event")
    description = models.CharField(max_length=500, default = "No Description Given")
    date = models.DateTimeField(auto_now_add=False)
    time = models.TimeField(auto_now_add=False)
    game = models.ForeignKey(Games,
        on_delete=models.SET_DEFAULT, default=1)
    creator = models.ForeignKey(Gamer,
        on_delete=models.SET_DEFAULT, default=1)
    attendees = models.ManyToManyField(Gamer, related_name="attending")
    eventstatus = models.ForeignKey("levelupapi.eventstatus",
        on_delete=models.SET_DEFAULT, default=1)
    
    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value