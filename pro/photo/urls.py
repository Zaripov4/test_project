from django.urls import path, include
from .views import ImageGalleryViewSet, AlbumViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('album', AlbumViewSet)
router.register(r'', ImageGalleryViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
