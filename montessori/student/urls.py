from django.urls import path

from .views import student_re_registration_view, student_detail_view, student_list_view

urlpatterns = [
    path("Enfants/", student_list_view, name='student_all'),
    path("Reinscription/<int:ambience_id>", student_re_registration_view, name='student_list'),
    path("Profil/<int:ambience_id>/<int:student_id>", student_detail_view, name='student_detail'),

    ]
