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

    def get_permissions(self):
        if self.action in ['create', 'activate']:
            self.permission_classes = [AllowAny]
        return super().get_permissions()

    def perform_create(self, serializer):
        super(UserViewSet, self).perform_create(serializer)
        user = serializer.instance
        user.set_password(serializer.validated_data['password'])
        user.save()
