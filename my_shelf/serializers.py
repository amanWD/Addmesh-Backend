from rest_framework import serializers

from .models import MyShelf


class MyShelfSerializers(serializers.ModelSerializer):
    class Meta:
        model = MyShelf
        fields = "__all__"