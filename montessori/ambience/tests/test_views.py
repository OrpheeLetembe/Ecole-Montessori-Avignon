from django import urls


def test_add_ambience(client, authenticated_user, ambience_data):
    add_ambience_url = urls.reverse('add_ambience')

    response = client.post(add_ambience_url, data=ambience_data)

    assert response.url == "/?next=/ambiance/ajouter"
    assert response.status_code == 302
