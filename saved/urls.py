from django.urls import path

from .views import get_blog, get_ebook, get_audio_book, get_explanation_audio, save_product

urlpatterns = [
    path("toggleSaveProduct/", save_product, name="toggle_save_product"),
    path("blogAPI/blogs/", get_blog, name="blog_saved"),
    path("ebookAPI/products/", get_ebook, name="ebook_saved"),
    path("audioBookAPI/products/", get_audio_book, name="audio_book_saved"),
    path("explanationAudioAPI/products/", get_explanation_audio, name="explanation_audio_saved"),
]