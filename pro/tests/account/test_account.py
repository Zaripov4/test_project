import pytest

from account.models import User

pytestmark = pytest.mark.django_db

USER_PAYLOAD = {
    'username': 'alex',
    'email': 'alex@gmail.com',
    'password': 'supersecret',
}

class TestUserModel:
    def test_crete_user(self):
        user = User.objects.create_user(**USER_PAYLOAD)

        assert user
        assert user.username == USER_PAYLOAD['username']
        assert user.email == USER_PAYLOAD['email']
        assert user.check_password(USER_PAYLOAD['password'])
    
    def test_create_super_user(self):
        user = User.objects.create_superuser(**USER_PAYLOAD)

        assert user
        assert user.username == USER_PAYLOAD['username']
        assert user.email == USER_PAYLOAD['email']
        assert user.is_staff
        assert user.is_superuser
        assert user.check_password(USER_PAYLOAD['password'])