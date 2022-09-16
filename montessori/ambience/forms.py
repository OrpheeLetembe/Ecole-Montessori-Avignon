from django import forms

from .models import Ambience


class AmbienceForm(forms.ModelForm):

    ENVIRONMENT_CHOICES = (
        ('BOIS', 'Bois'),
        ('TERRE', 'Terre'),

    )
    name = forms.ChoiceField(
        label="Nom",
        choices=ENVIRONMENT_CHOICES)
    date_start = forms.DateField(label="Date de début",
                                 widget=forms.DateInput( attrs={"class": "form-control",
                                                                'placeholder': 'jour/mois/année'}))
    date_end = forms.DateField(label="Date de fin",
                               widget=forms.DateInput(attrs={"class": "form-control",
                                                             'placeholder': 'jour/mois/année'}))

    note = forms.CharField(
        label="Commentaires", required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Ambience
        fields = ['name', 'date_start', 'date_end', 'note']

