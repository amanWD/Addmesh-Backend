from rest_framework import viewsets, filters

from .models import Blog, Attachments
from .serializers import BlogSerializer, AttachmentsSerializer


class BlogViewset(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']

class AttachmentsViewset(viewsets.ModelViewSet):
    queryset = Attachments.objects.all()
    serializer_class = AttachmentsSerializer