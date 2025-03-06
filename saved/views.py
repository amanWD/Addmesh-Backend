from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from base.models import Base

from blog.models import Blog
from blog.serializers import BlogSerializer

from ebook.models import Ebook
from ebook.serializers import EbookSerializer

from audio_book.models import AudioBook
from audio_book.serializers import AudioBookSerializer

from explanation_audio.models import ExplanationAudio
from explanation_audio.serializers import ExplanationAudioSerializer

from .models import Saved
from .serializers import SavedSerializers

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_blog(request):
    user = request.user
    user_saved = Saved.objects.filter(user=user)
    
    user_blog_saved = []

    for save in user_saved: 
        if (save.item.type == "blog"):
            blog = Blog.objects.filter(id=save.item.id).first()
            blog_json = BlogSerializer(blog, context={'request': request})
            user_blog_saved.append(blog_json.data)

    return Response(user_blog_saved, status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_ebook(request):
    user = request.user
    user_saved = Saved.objects.filter(user=user)
    
    user_ebook_saved = []

    for save in user_saved: 
        if (save.item.type == "ebook"):
            ebook = Ebook.objects.filter(id=save.item.id).first()
            ebook_json = EbookSerializer(ebook, context={'request': request})
            user_ebook_saved.append(ebook_json.data)

    return Response(user_ebook_saved, status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_audio_book(request):
    user = request.user
    user_saved = Saved.objects.filter(user=user)
    
    user_audio_book_saved = []

    for save in user_saved: 
        if (save.item.type == "audio book"):
            audio_book = AudioBook.objects.filter(id=save.item.id).first()
            audio_book_json = AudioBookSerializer(audio_book, context={'request': request})
            user_audio_book_saved.append(audio_book_json.data)

    return Response(user_audio_book_saved, status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_explanation_audio(request):
    user = request.user
    user_saved = Saved.objects.filter(user=user)
    
    user_explanation_audio_saved = []

    for save in user_saved: 
        if (save.item.type == "explanation audio"):
            explanation_audio = ExplanationAudio.objects.filter(id=save.item.id).first()
            explanation_audio_json = ExplanationAudioSerializer(explanation_audio, context={'request': request})
            user_explanation_audio_saved.append(explanation_audio_json.data)

    return Response(user_explanation_audio_saved, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def save_product(request):
    user = request.user
    product_id = request.data.get("product_id")
    try:
        product = Base.objects.filter(id=product_id).first()

        if (Saved.objects.filter(user=user, item=product).exists()):
            product_saved = Saved.objects.filter(user=user, item=product)
            product_saved.delete()
            return Response({"message": "Removed Successfully From Saved!"}, status=status.HTTP_200_OK)
        else:
            product_saved = Saved.objects.create(user=user, item=product)
            product_saved.save()

        return Response({"message": "Saved Successfully!"}, status=status.HTTP_200_OK)
    except:
        return Response({"error": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

    