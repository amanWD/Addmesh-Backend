from rest_framework.routers import SimpleRouter

from .views import BlogViewset, AttachmentsViewset

router = SimpleRouter()
router.register("blogs", BlogViewset, basename="blog") 
router.register("attachments", AttachmentsViewset, basename="attachments") 

urlpatterns = router.urls