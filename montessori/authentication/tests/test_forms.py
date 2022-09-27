from django.contrib.auth import get_user_model

from authentication.forms import SignUpForm


def test_signup_form_validate_and_save(user_data):

    """
    In the first assert, testing the SignUpForm to check if the user input data is properly
    validated or not.
    For the second assert, we are checking if the User object is created properly
    by using SignUpForm or not
    """
    user_model = get_user_model()

    form = SignUpForm(data=user_data)
    assert form.is_valid()

    test_user = form.save()
    assert isinstance(test_user, user_model)
