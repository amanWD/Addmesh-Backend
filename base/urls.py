from rest_framework.routers import SimpleRouter

from .views import BaseViewset

router = SimpleRouter()
router.register("", BaseViewset, basename="base")

urlpatterns = router.urls