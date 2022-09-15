from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Students
from ambience.models import Ambience
from .forms import StudentForm


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


@login_required
def student_detail_view(request, student_id, ambience_id):
    ambience = Ambience.objects.get(id=ambience_id)
    student = Students.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
    else:
        form = StudentForm(instance=student)
    context = {
        'form': form,
        'ambience': ambience,
        'student': student
    }

    return render(request, 'student/student_profil.html', context=context)
