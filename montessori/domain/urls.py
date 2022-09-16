from django.urls import path
from .views import practical_life_view, sensorial_mat_view, mathematique_view, \
    langage_letter_view, show_case_view, print_student_case_view, student_bilan_pdf_view
urlpatterns = [
    path("Vie pratique/<int:ambience_id>/<int:student_id>",
         practical_life_view, name='practical_life'),
    path("Materiel Sensoriel/<int:ambience_id>/<int:student_id>",
         sensorial_mat_view, name='sensorial_mat'),
    path("Mathematiques/<int:ambience_id>/<int:student_id>",
         mathematique_view, name='mathes'),
    path("Langage/<int:ambience_id>/<int:student_id>",
         langage_letter_view, name='langage'),
    path("Dossier/<int:ambience_id>/<int:student_id>",
         show_case_view, name='student_case'),
    path("Dossier-imprimer/<int:ambience_id>/<int:student_id>",
         print_student_case_view, name='print_case'),
    path("Bilan-imprimer/<int:ambience_id>/<int:student_id>",
         student_bilan_pdf_view, name='print_choice'),
]
