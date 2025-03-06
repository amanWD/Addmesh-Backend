from django.urls import path

from .views import get_ebook, get_audio_book, get_explanation_audio

urlpatterns = [
    path("ebookAPI/products/", get_ebook, name="ebook_my_shelf"),
    path("audioBookAPI/products/", get_audio_book, name="audio_book_my_shelf"),
    path("explanationAudioAPI/products/", get_explanation_audio, name="explanation_audio_my_shelf"),
]