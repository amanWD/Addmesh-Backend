from rest_framework import viewsets

from .models import Base
from .serializers import BaseSerializer


class BaseViewset(viewsets.ModelViewSet):
    queryset = Base.objects.all()
    serializer_class = BaseSerializer