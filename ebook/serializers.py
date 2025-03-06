from rest_framework import serializers
from my_shelf.models import MyShelf
from saved.models import Saved

from .models import Ebook


class EbookSerializer(serializers.ModelSerializer):
    is_bought = serializers.SerializerMethodField()
    is_saved = serializers.SerializerMethodField()

    class Meta: 
        model = Ebook
        fields = ["id", "title", "type", "description", "price_in_etb", "price_in_usd", "created_at", "updated_at", "image", "ebook_file", "is_bought", "is_saved"]

    def get_is_bought(self, obj):
        user = self.context.get("request").user

        if user.is_authenticated:
            return MyShelf.objects.filter(user=user, item=obj).exists()
        return False
    
    def get_is_saved(self, obj):
        user = self.context.get("request").user

        if user.is_authenticated:
            return Saved.objects.filter(user=user, item=obj).exists()
        return False