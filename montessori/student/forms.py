from django import forms
from .models import Students


class StudentForm(forms.ModelForm):

    photo = forms.ImageField(
        label="Photo", required=False,
        widget=forms.FileInput(attrs={"class": "form-control"}))
    firstname = forms.CharField(
        label="Prénom", widget=forms.TextInput(attrs={"class": "form-control"}))
    lastname = forms.CharField(
        label="Nom", widget=forms.TextInput(attrs={"class": "form-control"}))
    date_of_birth = forms.DateField(
        label="Date de naissance", input_formats=['%d/%m/%Y'])
    profil = forms.CharField(
        label="Profil", required=False,
        widget=forms.Textarea(attrs={"rows": 8, "cols": 81, 'class': 'form-control'}))

    class Meta:
        model = Students
        fields = ['photo', 'firstname', 'lastname', 'date_of_birth', 'profil']