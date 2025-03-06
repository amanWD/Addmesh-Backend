from rest_framework.routers import SimpleRouter

from .views import ExplanationAudioViewset, ChapterViewset, AudioFileViewset

router = SimpleRouter()

router.register("products", ExplanationAudioViewset, basename="explanation_audio")
router.register("chapters", ChapterViewset, basename="chapters")
router.register("audio_files", AudioFileViewset, basename="playlist")

urlpatterns = router.urls