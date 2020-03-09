from rest_framework import routers
from django.urls import path, include

from .views import LinkViewset

router = routers.DefaultRouter()
router.register('links', LinkViewset)

urlpatterns = router.urls
