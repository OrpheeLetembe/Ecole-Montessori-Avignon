from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=60, label="Nom d'utilisateur",
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(max_length=60, label="Mot de passe",
                               widget=forms.PasswordInput(attrs={"class": "form-control"}))


class SignUpForm(UserCreationForm):
    CHOICES = (
        ('educator', 'Educatrice'),
        ('assistant', 'Assistante')
    )

    username = forms.CharField(
        required=True, label="Nom d'utilisateur",
        widget=forms.TextInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(
        label="Prénom", widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(
        label="Nom", widget=forms.TextInput(attrs={"class": "form-control"}))
    role = forms.ChoiceField(
        label="Rôle", required=False,
        choices=CHOICES, widget=forms.Select(attrs={"class": "form-control"}))
    password1 = forms.CharField(
        label="Mot de passe", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(
        label="Confirmation mot de passe",
        widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta(UserCreationForm.Meta):
        model = get_user_model()

    def save(self, commit=True):

        user = super().save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.role = self.cleaned_data["role"]
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
