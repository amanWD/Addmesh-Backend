from rest_framework import serializers

from my_shelf.models import MyShelf
from saved.models import Saved

from .models import ExplanationAudio, Chapter, AudioFile
        

class ChapterSerializer(serializers.ModelSerializer):
    playlist = serializers.SerializerMethodField()

    class Meta:
        model = Chapter
        fields = ['name', 'playlist']

    def get_playlist(self, obj):
        return list(obj.playlist.values_list("audio_file", flat=True))


class ExplanationAudioSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializer(many=True, read_only=True)
    is_bought = serializers.SerializerMethodField()
    is_saved = serializers.SerializerMethodField()

    class Meta:
        model = ExplanationAudio
        fields = ['id', 'title', 'description', 'type', 'image', 'price_in_etb', 'price_in_usd', 'created_at', 'updated_at', 'chapters', 'is_bought', 'is_saved']

    
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
        fields = ['id', 'audio_file', 'playlist']