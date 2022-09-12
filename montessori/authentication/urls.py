from django.urls import path

from .views import signup_page_view, login_page_view, logout_page_view, profile_page_view

urlpatterns = [
    path("", login_page_view, name='login'),
    path('Inscription/', signup_page_view, name='signup'),
    path('Deconnexion/', logout_page_view, name='logout'),
    path('Profil/', profile_page_view, name='user_profil'),
]