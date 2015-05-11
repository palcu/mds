from django.http import HttpResponse
from django.shortcuts import render

from .models import Material, Teacher


def index(request):
    teachers = []
    for teacher in Teacher.objects.all():
        courses = [str(x) for x in teacher.course_set.all()]
        teacher_context = {
            'name': teacher.name,
            'courses': ', '.join(courses),
        }
        teachers.append(teacher_context)

    return render(request, 'teme/index.html', {
        'materials': Material.objects.all(),
        'teachers': teachers,
    })
