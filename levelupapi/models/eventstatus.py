from cProfile import label
from django.db import models
class EventStatus(models.Model):
  label = models.CharField(max_length=50)