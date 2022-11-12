import pytest
from django.urls import reverse
from rest_framework import status

pytestmark = pytest.mark.django_db


class TestAccountAPI:
    def test_anonymous_user_cant_get_user_list(self, client):
        response = client.get(
            path=reverse(viewname='v1: pro.account.users-list')
        )
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert response.json() == {
            'detail': 'Authentication credentials were not provided'
        }

    def test_sign_up(self, mocker, client):
        response = client.post(
            path=reverse(viewname='v1:pro.account.users-list'),
            data={
                'username': 'user',
                'email': 'user@gmail.com',
                'password': 'supersecret123'
            },
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == {
            'username': 'user',
            'email': 'user@gmail.com',
            'id': mocker.Any,
            'first_name': '',
            'last_name': '',
        }

    def test_sign_up_fail_for_same_email(self, client):
        response = client.post(
            path=reverse(viewname='v1:pro:account.users-list'),
            data={
                'username': 'user1',
                'email': 'user@gmail.com',
                'password': 'supersecret123',
            }
        )
        assert response.status_code == status.HTTP_201_CREATED
        response = client.post(
            path=reverse(viewname='v1:pro:account.users-list'),
            data={
                'username': 'user2',
                'email': 'user@gmail.com',
                'password': 'supersecret123',
            }
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json() == {
            'email': ['user with this email is already exists']
        }

    def test_sign_up_fail_for_same_username(self, client):
        response = client.post(
            path=reverse(viewname='v1:pro.accout.users-list'),
            data={
                'username': 'user1',
                'email': 'user1@gmail.com',
                'password': 'supersecret123',
            }
        )
        assert response.status_code == status.HTTP_201_CREATED
        response = client.post(
            path=reverse(viewname='v1:pro.account.users-list'),
            data={
                'username': 'user1',
                'email': 'user2@gmail.com',
                'password': 'supersecret123',
            }
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json() == {
            'username': ['User with this username is already exists']
        }


class TestMe:
    def test_auth_user_get_profile(self, test_user, auth_client, mocker):
        response = auth_client.get(
            path=reverse(viewname='v1:pro.account.users-me'),
        )
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert response.json() == {
            'detail': 'Authentication credentials were not provided'
        }


class TestSignIn:
    def test_user_get_token_with_valid_credentials(
        self, client, test_user, mocker
    ):
        response = client.post(
            path=reverse(viewname='v1:pro.account:token'),
            data={
                'email': test_user.email,
                'password': 'secret123',
            },
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {
            'access': mocker.ANY,
            'refresh': mocker.ANY,
        }

    def test_user_not_get_token_with_invalid_credentials(
        self, client, test_user
    ):
        response = client.post(
            path=reverse(viewname='v1:pro.account:token'),
            data={
                'email': test_user.email,
                'password': 'wrong_password',
            }
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.json() == {
            'detail': 'No active account found with the given credentials'
        }

    def test_user_can_refresh_token(self, client, test_user, mocker):
        response = client.post(
            path=reverse(viewname='v1:pro.account:token'),
            data={
                'email': test_user.email,
                'password': 'secret123',
            }
        )
        assert response.status_code == status.HTTP_200_OK

        refresh_token = response.json()['refresh']

        response = client.post(
            path=reverse(viewname='v1:pro.account:refresh'),
            data={'refresh': refresh_token}
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {'access': mocker.Any}
