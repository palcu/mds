import random

from django.core.management.base import BaseCommand
from teme.models import Course, Rating, Teacher


class Command(BaseCommand):
    def handle(self, *args, **options):
        names = ['Alex', 'Andrei', 'Adi', 'Iulia', 'Marius']
        courses = ['ASC', 'SD', 'TW', 'PP', 'PD']
        for i, name in enumerate(names):
            t = Teacher(name=name)
            t.save()
            c = Course(name=courses[i], teacher=t)
            c.save()
            r = Rating(grade=random.randint(0, 4), course=c)
