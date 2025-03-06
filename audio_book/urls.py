from rest_framework.routers import SimpleRouter

from .views import AudioBookViewset, AudioFileViewset

router = SimpleRouter()
router.register("products", AudioBookViewset, basename="audio_book")
router.register("audio_file", AudioFileViewset, basename="audio_file")

urlpatterns = router.urls