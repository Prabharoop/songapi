from django.shortcuts import render
from rest_framework import generics
from .models import Songs
from .serializers import SongSerializer
# Create your views here.

class ListSong(generics.ListCreateAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongSerializer

class DetailSong(generics.RetrieveUpdateDestroyAPIView):
        queryset = Songs.objects.all()
        serializer_class = SongSerializer
