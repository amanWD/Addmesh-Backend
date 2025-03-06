from rest_framework.routers import SimpleRouter

from .views import EbookViewSet

router = SimpleRouter()
router.register("products", EbookViewSet, basename="ebook")

urlpatterns = router.urls