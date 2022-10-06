from django.contrib.auth import get_user_model
from datetime import datetime

import pytest


@pytest.fixture
def user_data(db):
    return {
        'username': 'TestUser',
        'first_name': 'Test',
        'last_name': 'User',
        'role': 'educator',
        'password1': 'TestPassword',
        'password2': 'TestPassword'
    }


@pytest.fixture
def authenticated_user(client, db, user_data):
    user_model = get_user_model()
    test_user = user_model.objects.create_user(user_data)
    test_user.set_password(user_data.get('password1'))
    test_user.save()
    client.login()
    return test_user


def convert_to_date(date_time):
    """
    convert string to date
    :param date_time:
    :return:
    """
    date_format = "%d/%m/%Y"
    datetime_str = datetime.strptime(date_time, date_format)
    return datetime_str


@pytest.fixture
def ambience_data(db):

    date_start = "1/09/2022"
    convert_date_start = convert_to_date(date_start)

    date_end = "30/06/2023"
    convert_date_end = convert_to_date(date_end)

    return {
        'name': 'TERRE',
        'date_start': convert_date_start,
        'date_end': convert_date_end,

    }
