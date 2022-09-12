from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import os
import datetime
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


from .models import PracticalLife, SensoryMaterial, Math, Langage, Letter
from student.models import Students
from ambience.models import Ambience
from . import forms


def get_ambience(id):
    ambience = Ambience.objects.get(id=id)
    return ambience


def get_student(id):
    student = Students.objects.get(id=id)
    return student


@login_required
def practical_life_view(request, student_id, ambience_id):
    ambience = get_ambience(id=ambience_id)
    student = get_student(id=student_id)
    practical_life_student = PracticalLife.objects.get(Q(student=student) & Q(date_start=ambience.date_start))
    if request.method == 'POST':
        form = forms.PracticalLifeForm(request.POST, instance=practical_life_student)
        if form.is_valid():
            form.save()
            #return redirect('practical_life', ambience_id=ambience_id, student_id=student_id)
    else:
        form = forms.PracticalLifeForm(instance=practical_life_student)
    context = {
        'form': form,
        'pls': practical_life_student,
        'student': student,
        'ambience': ambience
    }
    return render(request, 'domain/practical_life.html', context)


@login_required
def sensorial_mat_view(request, ambience_id, student_id):
    ambience = get_ambience(id=ambience_id)
    student = get_student(id=student_id)
    sensorial_mat_student = SensoryMaterial.objects.get(Q(student=student) &
                                                        Q(date_start=ambience.date_start))
    if request.method == 'POST':
        form = forms.SensoryMaterialForm(request.POST, instance=sensorial_mat_student)
        if form.is_valid():
            form.save()
            #return redirect('sensorial_mat', ambience_id=ambience_id, student_id=student_id)
    else:
        form = forms.SensoryMaterialForm(instance=sensorial_mat_student)
    context = {
        'form': form,
        'mss': sensorial_mat_student,
        'student': student,
        'ambience': ambience
    }
    return render(request, 'domain/sensorial_mat.html', context)


@login_required
def mathematique_view(request, ambience_id, student_id):
    ambience = get_ambience(id=ambience_id)
    student = get_student(id=student_id)
    maths_student = Math.objects.get(Q(student=student) & Q(date_start=ambience.date_start))
    if request.method == 'POST':
        form = forms.MathForm(request.POST, instance=maths_student)
        if form.is_valid():
            form.save()
            #return redirect('mathes', ambience_id=ambience_id, student_id=student_id)
    else:
        form = forms.MathForm(instance=maths_student)
    context = {
        'form': form,
        'mts': maths_student,
        'student': student,
        'ambience': ambience
    }
    return render(request, 'domain/mathes.html', context)


@login_required
def langage_letter_view(request, ambience_id, student_id):
    ambience = get_ambience(id=ambience_id)
    student = get_student(id=student_id)
    langage_student = Langage.objects.get(Q(student=student) & Q(date_start=ambience.date_start))
    letter_student = Letter.objects.get(Q(student=student) & Q(date_start=ambience.date_start))

    if request.method == 'POST':
        langage_form = forms.LangageForm(request.POST, instance=langage_student)
        letter_form = forms.LetterForm(request.POST, instance=letter_student)
        if all([langage_form.is_valid(), letter_form.is_valid()]):
            langage_form.save()
            letter_form.save()
            #return redirect('Langage', ambience_id=ambience_id, student_id=student_id)
    else:
        langage_form = forms.LangageForm(instance=langage_student)
        letter_form = forms.LetterForm(instance=letter_student)

    context = {
        'langage_form': langage_form,
        'letter_form': letter_form,
        'mts': langage_student,
        'student': student,
        'ambience': ambience
    }
    return render(request, 'domain/langage.html', context)


@login_required
def show_case_view(request, ambience_id, student_id):
    ambience = get_ambience(id=ambience_id)
    student = get_student(id=student_id)
    practical_life_student = PracticalLife.objects.get(Q(student=student) &
                                                       Q(date_start=ambience.date_start))
    sensorial_mat_student = SensoryMaterial.objects.get(Q(student=student) &
                                                        Q(date_start=ambience.date_start))
    maths_student = Math.objects.get(Q(student=student) & Q(date_start=ambience.date_start))
    langage_student = Langage.objects.get(Q(student=student) & Q(date_start=ambience.date_start))
    letter_student = Letter.objects.get(Q(student=student) & Q(date_start=ambience.date_start))

    pls = practical_life_student
    mss = sensorial_mat_student
    mathes = maths_student
    lang = langage_student
    lt = letter_student

    context = {
        'student': student,
        'pls': pls,
        'mss': mss,
        'mts': mathes,
        'lang': lang,
        'lt': lt,
        'ambience': ambience
    }

    return render(request, 'domain/student_case.html', context=context)


@login_required
def print_student_case_view(request, ambience_id, student_id):
    """ This function allows the export of a child’s file in pdf format."""
    ambience = get_ambience(id=ambience_id)
    student = get_student(id=student_id)
    practical_life_student = PracticalLife.objects.get(Q(student=student) & Q(date_start=ambience.date_start))
    sensorial_mat_student = SensoryMaterial.objects.get(Q(student=student) & Q(date_start=ambience.date_start))
    maths_student = Math.objects.get(Q(student=student) & Q(date_start=ambience.date_start))
    langage_student = Langage.objects.get(Q(student=student) & Q(date_start=ambience.date_start))
    letter_student = Letter.objects.get(Q(student=student) & Q(date_start=ambience.date_start))

    pls = practical_life_student
    mss = sensorial_mat_student
    mathes = maths_student
    lang = langage_student
    lt = letter_student
    template_path = 'domain/case_pdf.html'
    context = {
        'student': student,
        'pls': pls,
        'mss': mss,
        'mts': mathes,
        'lang': lang,
        'lt': lt,
        'ambience': ambience
    }
    response = HttpResponse(content_type='application/pdf')
    filename = "{}_{}".format(student, student.ambience)
    response['Content-Disposition'] = 'attachment; filename=%s.pdf' % filename
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
        html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def trim_choice(data, activity):
    """This function allows you to choose the observations to be printed according to the quarter.
     It takes in parameter the data of the post request
     and the desired activity and returns the observations of the quarter.
     """

    if data is not None:
        if data == "observations_1":
            trimestre = activity.observations_1
            return trimestre
        if data == "observations_2":
            trimestre = activity.observations_2
            return trimestre
        if data == "observations_3":
            trimestre = activity.observations_3
            return trimestre
    else:
        return ""


@login_required
def student_bilan_pdf_view(request, ambience_id, student_id):
    """ This function allows the creation of a child’s report in pdf format."""
    user = request.user
    ambience = get_ambience(id=ambience_id)
    student = get_student(id=student_id)
    practical_life_student = PracticalLife.objects.get(Q(student=student) & Q(date_start=ambience.date_start))
    sensorial_mat_student = SensoryMaterial.objects.get(Q(student=student) & Q(date_start=ambience.date_start))
    maths_student = Math.objects.get(Q(student=student) & Q(date_start=ambience.date_start))
    langage_student = Langage.objects.get(Q(student=student) & Q(date_start=ambience.date_start))

    today = datetime.date.today()
    form = forms.PrintFrom()
    if request.method == "POST":
        form = forms.PrintFrom(request.POST)
        if form.is_valid():
            trim_pratique_life = request.POST.get('pratique_life')
            trim_sensorial_material = request.POST.get('sensorial_material')
            trim_mathe = request.POST.get('mathe')
            trim_langage = request.POST.get('langage')
            pls = trim_choice(trim_pratique_life, practical_life_student)
            mss = trim_choice(trim_sensorial_material, sensorial_mat_student)
            mathes = trim_choice(trim_mathe, maths_student)
            lang = trim_choice(trim_langage, langage_student)
            template_path = 'domain/student_balance.html'
            context = {
                'user': user,
                'student': student,
                'today': today,
                'pls': pls,
                'mss': mss,
                'mathes': mathes,
                'lang': lang,
                'form': form,
                'ambience': ambience
            }
            response = HttpResponse(content_type='application/pdf')
            filename = "{}_{}".format(student, student.ambience)
            response['Content-Disposition'] = 'attachment; filename=Bilan_%s.pdf' % filename
            template = get_template(template_path)
            html = template.render(context)

            pisa_status = pisa.CreatePDF(
               html, dest=response)

            if pisa_status.err:
                return HttpResponse('We had some errors <pre>' + html + '</pre>')
            return response
    context = {
        'form': form,
        'student': student,
        'ambience': ambience

    }
    return render(request, 'domain/print_choice.html', context=context)
