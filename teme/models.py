from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=200)


class Course(models.Model):
    name = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher)


class Rating(models.Model):
    grade = models.IntegerField(validators=[MinValueValidator(1),
                                            MaxValueValidator(5)])
    course = models.ForeignKey(Course)
