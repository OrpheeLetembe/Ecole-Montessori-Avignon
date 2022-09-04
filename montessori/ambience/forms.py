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
    date_start = forms.CharField(
        label="Début", widget=forms.TextInput(attrs={"class": "form-control"}))
    date_end = forms.CharField(
        label="Fin", widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Ambience
        fields = ['name', 'date_start', 'date_end']

