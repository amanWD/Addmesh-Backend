from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/account/', include("accounts.urls")),
    path('v1/library/', include("base.urls")),
    path('v1/library/blogAPI/', include("blog.urls")),
    path('v1/library/ebookAPI/', include("ebook.urls")),
    path('v1/library/audioBookAPI/', include("audio_book.urls")), 
    path('v1/library/explanationAudioAPI/', include("explanation_audio.urls")), 
    path('v1/library/eventAPI/', include("event.urls")),
    path('v1/orderAPI/', include("orders.urls")), 
    path('v1/paypalAPI/', include("paypal_payment.urls")), 
    path('v1/my-shelf/', include("my_shelf.urls")), 
    path('v1/saved/', include("saved.urls")), 
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
