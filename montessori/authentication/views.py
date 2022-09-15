from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


from .forms import SignUpForm, LoginForm, EditProfileForm, ChangePasswordsForm


def signup_page_view(request):
    """This function allows the registration of a new user.
       After entering his credentials, the user is redirected to the ambiances page.
       """
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('ambience')
        else:
            form = SignUpForm()

    return render(request, "authentication/signup.html", {"form": form})


def login_page_view(request):
    """
    his function allows a registered user to log in.
    After verifying his credentials,
    the user is redirected to the ambiances page if they are correct.

    """
    form = LoginForm()
    message = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect('ambience')
            else:
                message = "Identifiants invalides."
    context = {
        'form': form,
        'message': message,

    }
    return render(request, "authentication/login.html", context=context)


def logout_page_view(request):
    """
    Function allowing the disconnection of a user.
    After disconnection, the user is redirected to the login page
    """
    logout(request)
    return redirect('login')


@login_required
def profile_page_view(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'authentication/user_profil.html', {'form': form})


@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = ChangePasswordsForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('user_profil')
    else:
        form = ChangePasswordsForm(request.user)

    return render(request, 'authentication/change_password.html', {'form': form})
