from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from ebook.models import Ebook
from ebook.serializers import EbookSerializer

from audio_book.models import AudioBook
from audio_book.serializers import AudioBookSerializer

from explanation_audio.models import ExplanationAudio
from explanation_audio.serializers import ExplanationAudioSerializer

from .models import MyShelf
from .serializers import MyShelfSerializers


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_ebook(request):
    user = request.user
    user_shelf = MyShelf.objects.filter(user=user)
    
    user_ebook_shelf = []

    for shelf in user_shelf: 
        if (shelf.item.type == "ebook"):
            ebook = Ebook.objects.filter(id=shelf.item.id).first()
            ebook_json = EbookSerializer(ebook, context={'request': request})
            user_ebook_shelf.append(ebook_json.data)

    return Response(user_ebook_shelf, status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_audio_book(request):
    user = request.user
    user_shelf = MyShelf.objects.filter(user=user)
    
    user_audio_book_shelf = []

    for shelf in user_shelf: 
        if (shelf.item.type == "audio book"):
            audio_book = AudioBook.objects.filter(id=shelf.item.id).first()
            audio_book_json = AudioBookSerializer(audio_book, context={'request': request})
            user_audio_book_shelf.append(audio_book_json.data)

    return Response(user_audio_book_shelf, status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_explanation_audio(request):
    user = request.user
    user_shelf = MyShelf.objects.filter(user=user)
    
    user_explanation_audio_shelf = []

    for shelf in user_shelf: 
        if (shelf.item.type == "explanation audio"):
            explanation_audio = ExplanationAudio.objects.filter(id=shelf.item.id).first()
            explanation_audio_json = ExplanationAudioSerializer(explanation_audio, context={'request': request})
            user_explanation_audio_shelf.append(explanation_audio_json.data)

    return Response(user_explanation_audio_shelf, status=status.HTTP_200_OK)