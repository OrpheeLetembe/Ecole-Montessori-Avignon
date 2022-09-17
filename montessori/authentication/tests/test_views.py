from django import urls
from django.contrib.auth import get_user_model
import pytest


@pytest.mark.parametrize('param', [
    'signup',
    'login',
])
def test_render_views(client, param):
    temp_url = urls.reverse(param)
    response = client.get(temp_url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_signup(client, user_data):
    user_model = get_user_model()
    assert user_model.objects.count() == 0

    signup_url = urls.reverse('signup')
    response = client.post(signup_url, user_data)
    assert user_model.objects.count() == 1
    assert response.status_code == 302
    assert response.url == urls.reverse('ambience')


@pytest.mark.django_db
def test_user_login(client, user_data):
    user_model = get_user_model()
    assert user_model.objects.count() == 0

    signup_url = urls.reverse('signup')
    temp_user = client.post(signup_url, user_data)
    assert user_model.objects.count() == 1

    login_url = urls.reverse('login')
    response = client.post(login_url, data={'username': user_data['username'],
                                            'password': user_data['password1']})
    assert response.status_code == 302
    assert response.url == urls.reverse('ambience')
