from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Students
from ambience.models import Ambience


@login_required
def student_list_view(request, ambience_id):
    """ This function allows you to get the list of atmospheres, the most recent ones first."""
    ambience = Ambience.objects.get(id=ambience_id)
    students = Students.objects.all().order_by('lastname')
    context = {
        'ambience': ambience,
        'students': students
    }
    return render(request, 'student/student_all.html', context=context)


