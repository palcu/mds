from django.contrib import admin

from .models import Teacher, Course, Rating


admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Rating)
