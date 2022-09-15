from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from student.models import Students
from domain.models import PracticalLife, SensoryMaterial, Math, Langage, Letter
from .models import Ambience
from .forms import AmbienceForm
from student.forms import StudentForm


@login_required
def ambiance_list_view(request):
    """ This function allows you to get the list of atmospheres, the most recent ones first."""
    user = request.user
    ambiences = Ambience.objects.filter(user=user).order_by('-date_start')
    return render(request, 'ambience/ambience_all.html', {'ambiences': ambiences})


@login_required
def ambiance_detail_view(request, pk):
    user = request.user
    ambience = Ambience.objects.get(id=pk)
    students = Students.objects.filter(ambience=ambience).order_by('lastname')
    context = {
        'ambience': ambience,
        'students': students,
        'user': user

    }
    return render(request, 'ambience/ambience_detail.html', context=context)


@login_required
def add_ambiance_view(request):
    """This function allows the connected user to add a new school year to his atmosphere"""

    form = AmbienceForm()
    if request.method == 'POST':
        form = AmbienceForm(request.POST)
        if form.is_valid():
            ambience = form.save(commit=False)
            ambience.user = request.user
            ambience.save()
            return redirect('ambience')
    context = {
        'form': form,
    }
    return render(request, 'ambience/add_ambience.html', context=context)


@login_required
def add_new_student_view(request, pk):
    """
        This function allows the creation of a new child object,
        as well as the creation of the practical life, sensory material,
        mathematics, language and letter objects associated with it
        """
    ambience = Ambience.objects.get(id=pk)
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.ambience.add(ambience)
            student.save()

            PracticalLife.objects.create(student=student, date_start=ambience.date_start)
            SensoryMaterial.objects.create(student=student, date_start=ambience.date_start)
            Math.objects.create(student=student, date_start=ambience.date_start)
            Langage.objects.create(student=student, date_start=ambience.date_start)
            Letter.objects.create(student=student, date_start=ambience.date_start)

            return redirect('ambience_detail', id=ambience.id)

    context = {
        'form': form,
        'ambience': ambience,

    }
    return render(request, 'ambience/add_student.html', context=context)


@login_required
def change_ambience_student_view(request, ambience_id, student_id):
    ambience = Ambience.objects.get(id=ambience_id)
    student = Students.objects.get(id=student_id)
    student.ambience.add(ambience)
    student.save()
    return redirect('student_list', ambience_id=ambience.id)
