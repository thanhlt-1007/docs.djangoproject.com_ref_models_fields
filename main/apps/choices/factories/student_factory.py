from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice

from main.apps.choices.models import Student


class StudentFactory(DjangoModelFactory):
    year_in_school = FuzzyChoice(Student.YEAR_IN_SCHOOL_CHOICES.keys())

    class Meta:
        model = Student
