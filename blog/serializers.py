from rest_framework import serializers

from saved.models import Saved
from .models import Blog, Attachments


class AttachmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachments
        fields = ["id", "reference_name", "image", "blog"]


class BlogSerializer(serializers.ModelSerializer):
    attachments = AttachmentsSerializer(many=True, read_only=True)
    is_saved = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ["id", "title", "description", "tag", "created_at", "updated_at", "attachments", "is_saved"]
    
     
    def get_is_saved(self, obj):
        user = self.context.get("request").user

        if user.is_authenticated:
            return Saved.objects.filter(user=user, item=obj).exists()
        return False