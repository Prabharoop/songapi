from rest_framework import serializers
from .models import Songs

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','song','artist','comments')
        model = Songs
