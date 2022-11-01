from django.urls import path, include
from rest_framework.routers import SimpleRouter
from account.views import UserViewSet

router = SimpleRouter()
router.register('', UserViewSet)

urlpatterns = [
      path('', include(router.urls)),
]