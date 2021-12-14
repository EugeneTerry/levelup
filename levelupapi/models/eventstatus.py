from django.db import models
class EventStatus(models.Model):
  eventstatus = models.CharField(max_length=50)