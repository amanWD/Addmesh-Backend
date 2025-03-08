from rest_framework import viewsets

from .models import Base
from .serializers import BaseSerializer


class BaseViewset(viewsets.ModelViewSet):
    queryset = Base.objects.all()
    serializer_class = BaseSerializer

    def get_queryset(self):
        queryset = super().get_queryset() 
        item_type = self.request.query_params.get('type')
        length = self.request.query_params.get('len')

        if item_type and length:
            queryset = queryset.filter(type=item_type) 
            queryset = queryset.order_by('?')[:int(length)]

        return queryset
