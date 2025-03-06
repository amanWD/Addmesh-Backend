from rest_framework import serializers

from my_shelf.models import MyShelf
from saved.models import Saved

from .models import AudioBook, AudioFile


class AudioBookSerializer(serializers.ModelSerializer):
    playlist = serializers.SerializerMethodField()
    is_bought = serializers.SerializerMethodField()
    is_saved = serializers.SerializerMethodField()

    class Meta:
        model = AudioBook
        fields = ['id', 'title', 'description', 'type', 'image', 'price_in_etb', 'price_in_usd', 'created_at', 'updated_at', 'playlist', 'is_bought', 'is_saved']

    def get_playlist(self, obj):
        return obj.playlist.values_list("audio_file", flat=True)
    
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


class AudioFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioFile
        fields = '__all__'