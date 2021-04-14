from rest_framework import routers

from .viewsets import RecordViewSet

router = routers.SimpleRouter()
router.register('records', RecordViewSet)

urlpatterns = router.urls
