from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    model = User
    permission_classes = (IsAuthenticated, )

    def get_permission(self):
        if self.action in ['activate', 'create']:
            self.permission_classes[AllowAny]
        return super(UserViewSet, self).get_permission()

    def perform_create(self, serializer):
        super(UserViewSet, self).perform_create(serializer)
        user = serializer.instance
        user.set_password(serializer.validated_date['password'])
        user.save(updated_fields=['password'])
