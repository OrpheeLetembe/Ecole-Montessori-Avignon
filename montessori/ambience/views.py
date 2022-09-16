from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from copy import deepcopy
from datetime import date

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
    today = date.today()
    ambience = Ambience.objects.get(id=pk)
    students = Students.objects.filter(ambience=ambience).order_by('lastname')
    if request.method == 'POST':
        form = AmbienceForm(request.POST, instance=ambience)
        if form.is_valid():
            form.save()
    else:
        form = AmbienceForm(instance=ambience)
    context = {
        'today': today,
        'form': form,
        'ambience': ambience,
        'students': students,
        'user': user

    }
    return render(request, 'ambience/ambience_detail.html', context=context)


def update_ambience_view(request, pk):
    ambience = Ambience.objects.get(id=pk)
    if request.method == 'POST':
        form = AmbienceForm(request.POST, instance=ambience)
        if form.is_valid():
            form.save()
    else:
        form = AmbienceForm(instance=ambience)
    context = {
        'form': form,
        'ambience': ambience,
    }
    return render(request, 'ambience/update_ambience.html', context=context)


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
    date_start = str(ambience.date_start)[:4]
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            student.ambience.add(ambience)

            PracticalLife.objects.create(student=student, date_start=date_start)
            SensoryMaterial.objects.create(student=student, date_start=date_start)
            Math.objects.create(student=student, date_start=date_start)
            Langage.objects.create(student=student, date_start=date_start)
            Letter.objects.create(student=student, date_start=date_start)

            return redirect('ambience_detail', pk=ambience.id)

    context = {
        'form': form,
        'ambience': ambience,

    }
    return render(request, 'ambience/add_student.html', context=context)


def copy_and_save_domaine(domain, date_start):
    new_domain = deepcopy(domain)
    new_domain.pk = None
    new_domain.date_start = date_start
    new_domain.save()
    return new_domain


@login_required
def change_ambience_student_view(request, ambience_id, student_id):
    ambience = Ambience.objects.get(id=ambience_id)
    old_date = int(str(ambience.date_start)[:4]) - 1
    new_date = str(ambience.date_start)[:4]
    student = Students.objects.get(id=student_id)
    student.ambience.add(ambience)
    student.save()
    practical_life_student = PracticalLife.objects.get(Q(student=student) &
                                                       Q(date_start=old_date))
    sensorial_mat_student = SensoryMaterial.objects.get(Q(student=student) &
                                                        Q(date_start=old_date))
    maths_student = Math.objects.get(Q(student=student) & Q(date_start=old_date))
    langage_student = Langage.objects.get(Q(student=student) & Q(date_start=old_date))
    letter_student = Letter.objects.get(Q(student=student) & Q(date_start=old_date))

    new_practical_life_student = copy_and_save_domaine(practical_life_student, new_date)
    new_sensorial_mat_student = copy_and_save_domaine(sensorial_mat_student, new_date)
    new_maths_student = copy_and_save_domaine(maths_student, new_date)
    new_langage_student = copy_and_save_domaine(langage_student, new_date)
    new_letter_student = copy_and_save_domaine(letter_student, new_date)

    return redirect('student_list', ambience_id=ambience.id)
