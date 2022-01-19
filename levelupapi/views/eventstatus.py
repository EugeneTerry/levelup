from logging import exception
from multiprocessing import context
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers

from levelupapi.models.eventstatus import EventStatus
# from levelupapi.views.event import EventStatusSerializer

class EventStatusView(ViewSet):
  
  #http
  def list(self, request):
    statuses = EventStatus.objects.all()
    try:
      serializer = EventStatusSerializer(
      statuses,
      many=True,
      context={'request': request}
    )
      return Response(serializer.data)
    except Exception as ex:
      return HttpResponseServerError(ex)
      
  #http
  def retrieve(self, request,pk=None):
    pass

class EventStatusSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = EventStatus
    fields = ('id', 'label')