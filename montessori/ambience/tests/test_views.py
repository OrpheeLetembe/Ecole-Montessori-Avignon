from django import urls
import pytest

from ambience.models import Ambience


def test_add_ambience(client, authenticated_user, ambience_data):
    add_ambience_url = urls.reverse('add_ambience')

    response = client.post(add_ambience_url, data=ambience_data)
    print(response)
    assert response.url == "/?next=/ambiance/ajouter"
    assert response.status_code == 302
