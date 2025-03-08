from rest_framework import viewsets, filters

from .models import AudioBook, AudioFile
from .serializers import AudioBookSerializer, AudioFileSerializer


class AudioBookViewset(viewsets.ModelViewSet):
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']


class AudioFileViewset(viewsets.ModelViewSet):
    queryset = AudioFile.objects.all()
    serializer_class = AudioFileSerializer