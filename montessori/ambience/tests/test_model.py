from ambience.models import Ambience
from authentication.models import User
import pytest


@pytest.mark.django_db
def test_ambience_str():

    """
    Testing whether ambience's __str__ method is implemented properly
    """

    user = User.objects.create(
        username='TestUser',
        first_name='Test',
        last_name='User',
        role='educator',
        password='test-password',

    )

    ambience = Ambience.objects.create(
        name='Terre',
        date_start='2022-01-09',
        date_end='2023-05-10',
        user=user,

    )

    assert str(ambience) == f'{ambience.name} ' \
                            f'{str(ambience.date_start)[:4]}-{str(ambience.date_end)[:4]}'
