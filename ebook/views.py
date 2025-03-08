from rest_framework import viewsets, filters

from .serializers import EbookSerializer
from .models import Ebook


class EbookViewSet(viewsets.ModelViewSet):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']