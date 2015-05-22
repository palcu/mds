from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from .constants import MIN_RATING_STAR_VALUE, MAX_RATING_STAR_VALUE


class Teacher(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Rating(models.Model):
    grade = models.IntegerField(validators=[
        MinValueValidator(MIN_RATING_STAR_VALUE),
        MaxValueValidator(MAX_RATING_STAR_VALUE)])
    course = models.ForeignKey(Course)

    def __str__(self):
        return self.course.name + ' - ' + self.grade
