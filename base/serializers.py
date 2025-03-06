from rest_framework import serializers

from .models import Base


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = '__all__'

    def get_queryset(self):
        type = self.request.query_params.get("type")
        len = self.request.query_params.get("len")

        print(type, len)

        if (type == "blogs" and len == 3):
            print(type, len)