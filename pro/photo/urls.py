import imp
from pydoc import importfile
from django.urls import path, include
from .views import ImageGalleryViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'',ImageGalleryViewSet)

urlpatterns = [path('', include(router.urls))]
