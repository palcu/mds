from statistics import mean

from django.http import HttpResponse
from django.shortcuts import render

from .models import Course, Teacher, Rating

def get_courses(number):
    courses = []
    for course in Course.objects.all()[:number]:
        ratings = [x.grade for x in course.rating_set.all()]
        print(course.rating_set.all())
        course_context = {
            'name': course.name,
            'teacher': course.teacher.name,
            'rating': int(mean(ratings)) if len(ratings) else 3,
            'rating_count': course.rating_set.count()
        }
        courses.append(course_context)
    return courses


def get_teachers(number):
    teachers = []
    for teacher in Teacher.objects.all()[:number]:
        courses = []
        ratings = []
        for course in teacher.course_set.all():
            courses.append(str(course))
            ratings += [x.grade for x in course.rating_set.all()]

        teacher_context = {
            'name': teacher.name,
            'courses': ', '.join(courses),
            'rating': int(mean(ratings)) if len(ratings) else 3,
        }
        teachers.append(teacher_context)
    return teachers


def index(request):
    return render(request, 'teme/index.html', {
        'courses': get_courses(5),
        'teachers': get_teachers(5),
    })

def courses(request):
    return render(request, 'teme/courses.html', {
        'courses': get_courses(100),
    })

def teachers(request):
    return render(request, 'teme/teachers.html', {
        'teachers': get_teachers(100),
    })
