from django.db import models


class Student(models.Model):
    year_in_school = models.CharField(max_length=2)
