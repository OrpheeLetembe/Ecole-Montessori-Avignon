from django.urls import path

from .views import student_list_view, student_detail_view

urlpatterns = [
    path("Reinscription/<int:ambience_id>", student_list_view, name='student_list'),
    path("Profil/<int:ambience_id>/<int:student_id>", student_detail_view, name='student_detail'),

    ]
