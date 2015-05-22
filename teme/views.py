from statistics import mean

from django.http import HttpResponse
from django.shortcuts import render

from .models import Course, Teacher


def index(request):
    teachers = []
    for teacher in Teacher.objects.all()[:10]:
        courses = []
        ratings = []
        for course in teacher.course_set.all():
            courses.append(str(course))
            ratings += [x.grade for x in course.rating_set.all()]

        teacher_context = {
            'name': teacher.name,
            'courses': ', '.join(courses),
            'rating': int(mean(ratings)) if len(ratings) else 3
        }
        teachers.append(teacher_context)
    print(teachers)

    return render(request, 'teme/index.html', {
        'courses': Course.objects.all(),
        'teachers': teachers,
    })
