from django.urls import path

from .views import student_list_view

urlpatterns = [
    path("Reinscription/<int:ambience_id>", student_list_view, name='student_list'),

    ]
