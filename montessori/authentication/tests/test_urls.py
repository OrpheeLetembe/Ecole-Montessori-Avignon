from django.urls import reverse, resolve
from authentication.views import signup_page_view, login_page_view, logout_page_view


def test_signup_url():
    """
        Testing if the 'signup' route is mapping to SignUpView
    """
    url = reverse("signup")
    assert resolve(url).view_name == 'signup'
    assert resolve(url).func == signup_page_view


def test_login_url():
    """
        Testing if the 'login' route is mapping to LoginView
    """
    url = reverse("login")
    assert resolve(url).view_name == 'login'
    assert resolve(url).func == login_page_view


def test_logout_url():
    """
        Testing if the 'logout' route is mapping to logout_page
    """
    url = reverse("logout")
    assert resolve(url).view_name == 'logout'
    assert resolve(url).func == logout_page_view
