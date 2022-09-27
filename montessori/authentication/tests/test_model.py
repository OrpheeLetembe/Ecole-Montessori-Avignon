from django.contrib.auth import get_user_model


def test_user_str(user_data):

    """
    Testing whether User's __str__ method is implemented properly
    """
    user_model = get_user_model()
    test_user = user_model.objects.create_user(user_data)

    assert str(test_user) == f'{test_user.first_name} {test_user.last_name}'
