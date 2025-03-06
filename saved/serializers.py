from rest_framework import serializers

from base.models import Base
from .models import Saved


class SavedSerializers(serializers.ModelSerializer):

    def get_queryset(self):
        type = self.context.request.query_params.get('type')
        len = self.context.request.query_params.get('len')

        print(type, len)

        if (type == "blogs" and len == 3):
            return "Success" 

    class Meta:
        model = Saved
        fields = "__all__"