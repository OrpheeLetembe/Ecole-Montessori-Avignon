from django.urls import path

from . import views

urlpatterns = [
    path("ambiance/ajouter", views.add_ambiance_view, name='add_ambience'),
    path("ambiance", views.ambiance_list_view, name='ambience'),
    path("ambiance/<int:pk>", views.ambiance_detail_view, name='ambience_detail'),
    path("add/<int:pk>", views.add_new_student_view, name='add_student'),
    path("add/<int:ambience_id>/<int:student_id>", views.change_ambience_student_view,
         name='change_ambiance'),
    path("update_ambience/<int:pk>", views.update_ambience_view, name='update_ambience'),


]
