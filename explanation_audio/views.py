from rest_framework import viewsets, filters

from .models import ExplanationAudio, Chapter, AudioFile
from .serializers import ExplanationAudioSerializer, ChapterSerializer, AudioFileSerializer


class ExplanationAudioViewset(viewsets.ModelViewSet):
    queryset = ExplanationAudio.objects.all()
    serializer_class = ExplanationAudioSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']


class ChapterViewset(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

class AudioFileViewset(viewsets.ModelViewSet):
    queryset = AudioFile.objects.all()
    serializer_class = AudioFileSerializer