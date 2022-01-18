from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from levelupapi.models import Gamer
from levelupapi.views.event import EventSerializer


@api_view(['GET'])
def get_gamer_profile(request):
  gamer = request.auth.user.gamer
  
  serializer = GamerSerializer(gamer)
  return Response(serializer.data)

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for gamer's related Django user"""
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
class GamerSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    
    attending = EventSerializer(many = True)
    class Meta:
      model = Gamer
      fields = ('id', 'bio', 'user', 'attending')