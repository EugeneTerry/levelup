from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from levelupapi.models import Gamer
from levelupapi.views.event import EventSerializer

@api_view(['GET'])
def get_gamer_profile(request):
  gamer = request.auth.user.gamer
  
  serializer = GameSerializer(gamer)
  return Response(serializer.data)

class GameSerializer(serializers.ModelSerializer):
    
    class Meta:
      model = Gamer
      fields = ('id', 'bio', 'attending')