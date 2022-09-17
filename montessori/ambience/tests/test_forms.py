
from ambience.forms import AmbienceForm
from authentication.models import User

import pytest


@pytest.mark.django_db
def test_ambience_form_validate():

    """
    Testing the AmbienceForm to check if the user input data is properly validated or not
    """

    temp_ambience = {
        'name': 'Terre',
        'date_start': '1/09/2022',
        'date_end': '4/06/2023',

    }

    ambience = AmbienceForm(data=temp_ambience)

    assert ambience.is_valid()
