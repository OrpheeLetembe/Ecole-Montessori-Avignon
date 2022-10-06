from ambience.forms import AmbienceForm
from ambience.models import Ambience


def test_ambience_form_validate_and_save(ambience_data):

    """
     The first assert, testing the AmbienceForm to check if the user input data is properly
     validated or not
     The second assert, we are checking if the Ambience object is created properly
    by using AmbienceForm or not
    """

    form = AmbienceForm(data=ambience_data)
    assert form.is_valid()

    test_ambience = form.save(commit=False)

    assert isinstance(test_ambience, Ambience)
