from authentication.models import User
import pytest


@pytest.mark.django_db
def test_user_str():

    """
    Testing whether User's __str__ method is implemented properly
    """
    user = User.objects.create(
        username='TestUser',
        first_name='Test',
        last_name='User',
        role='educator',
        password='test-password',

    )

    assert str(user) == f'{user.first_name} {user.last_name}'
