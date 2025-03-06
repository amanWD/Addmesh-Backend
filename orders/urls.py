from rest_framework.routers import SimpleRouter

from .views import OrderViewset

router = SimpleRouter()
router.register("", OrderViewset, basename="order")

urlpatterns = router.urls