import pytest
from account.models import User
from rest_framework.validators import ValidationError

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

    @pytest.mark.parametrize(
        'username, email, password'
        [
            (None, None, None),
            ('alex', None, None),
            (None, 'alex@gmail.com'),
            (None, None, 'supersecret'),
            ('alex', 'alex@gmail.com', None),
            ('alex', None, 'supersecret'),
            (None, 'alex@gmail.com', 'supersecret'),
        ],
    )
    def test_invalid_data_does_not_create_user(
        self, username, email, password
    ):
        with pytest.raises(ValidationError) as exc:
            User.objects.create_user(**USER_PAYLOAD)
        assert exc.value.messages == [
            'Required fields username, email, password'
        ]
        assert User.objects.count() == 0

    def test_user_create_with_same_username_fails(self):
        with pytest.raises(ValidationError) as exc:
            User.objects.create_user(**USER_PAYLOAD)
        assert exc.value.messages == [
            'User with this username already exists'
        ]
        assert User.objects.count() == 1

    def test_user_create_with_same_email_fails(self):
        with pytest.raises(ValidationError) as exc:
            User.objects.create_user(**USER_PAYLOAD)
        assert exc.value.messages == [
            'User with this email is already exists'
        ]
        assert User.objects.count() == 1
