from django.contrib.auth import get_user_model

from ambience.forms import AmbienceForm
from ambience.models import Ambience


def test_ambience_form_validate_and_save(ambience_data):

    """
     The first assert, testing the AmbienceForm to check if the user input data is properly validated or not
     The second assert, we are checking if the Ambience object is created properly
    by using AmbienceForm or not
    """
    #user_model = get_user_model()
    #test_user = user_model.objects.create_user(user_data)

    form = AmbienceForm(data=ambience_data)
    assert form.is_valid()

    test_ambience = form.save(commit=False)
    #test_ambience.user = test_user

    assert isinstance(test_ambience, Ambience)
