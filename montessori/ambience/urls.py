from django.urls import path

from . import views

urlpatterns = [
    path("ambiance/ajouter", views.add_ambiance_view, name='add_ambience'),
    path("ambiance", views.ambiance_list_view, name='ambience'),
    path("ambiance/<int:id>", views.ambiance_detail_view, name='ambience_detail'),
    path("add/<int:id>", views.add_student_view, name='add_student'),

]