import pytest


@pytest.fixture
def user_data():
    return {
        'username': 'TestUser',
        'first_name': 'Test',
        'last_name': 'User',
        'role': 'educator',
        'password1': 'TestPassword',
        'password2': 'TestPassword'
    }
