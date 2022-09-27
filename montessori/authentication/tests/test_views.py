from django import urls
from django.contrib.auth import get_user_model
from django.contrib import auth
import pytest


@pytest.mark.parametrize('param', [
    'signup',
    'login',

])
def test_render_views(client, param):
    temp_url = urls.reverse(param)
    response = client.get(temp_url)
    assert response.status_code == 200


def test_user_signup(client, user_data):
    """
        In the first assert, we are checking if a user is created successfully then,
         the user is redirected to 'ambience/' route,
        For the second assert, we are checking the 302 status code(redirect)
        For the third assert, we are checking that the user is authenticated
    """
    user_model = get_user_model()
    assert user_model.objects.count() == 0

    signup_url = urls.reverse('signup')
    response = client.post(signup_url, user_data)
    assert user_model.objects.count() == 1

    assert response.url == urls.reverse('ambience')
    assert response.status_code == 302

    user = auth.get_user(client)
    assert user.is_authenticated


def test_user_login(client, user_data):
    """
        we check if a user is successfully logged in, then the user is redirected
        to the 'ambience/' route,
        For the second assertion, we check for status code 302 (redirect)
        For the third assert, we are checking that the user is authenticated
    """
    user_model = get_user_model()
    signup_url = urls.reverse('signup')
    temp_user = client.post(signup_url, user_data)
    assert user_model.objects.count() == 1

    login_url = urls.reverse('login')
    response = client.post(login_url, data={'username': user_data['username'],
                                            'password': user_data["password1"]})

    assert response.url == urls.reverse('ambience')
    assert response.status_code == 302

    user = auth.get_user(client)
    assert user.is_authenticated


def test_user_profil(client, authenticated_user):
    profil_url = urls.reverse('user_profil')
    response = client.get(profil_url)
    assert response.status_code == 302


def test_user_logout(client, authenticated_user):
    """
        Testing if our logout_view properly logouts user, In the first assert, we are checking if user is redirected to
        "login" route, for the second assert we are checking 302 redirect status code
    """
    logout_url = urls.reverse('logout')
    response = client.get(logout_url)

    assert response.url == urls.reverse('login')
    assert response.status_code == 302
