import factory

from main.apps.choices.models import Student


class StudentFactory(factory.django.DjangoModelFactory):
    year_in_school = factory.fuzzy.FuzzyChoice(Student.YEAR_IN_SCHOOL_CHOICES.keys())

    class Meta:
        model = Student
