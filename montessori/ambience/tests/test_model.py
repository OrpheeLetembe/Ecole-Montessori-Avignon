from ambience.models import Ambience
from django.contrib.auth import get_user_model


def test_ambience_str(ambience_data, user_data):

    """
    Testing whether ambience's __str__ method is implemented properly
    """
    user_model = get_user_model()
    test_user = user_model.objects.create_user(user_data)

    ambience = Ambience.objects.create(
        name='Terre',
        date_start='2022-01-09',
        date_end='2023-05-10',
        user=test_user,

    )

    assert str(ambience) == f'{ambience.name} ' \
                            f'{str(ambience.date_start)[:4]}-{str(ambience.date_end)[:4]}'
