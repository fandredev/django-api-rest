from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    rg = models.CharField(max_length=15)
    cpf = models.CharField(max_length=15)
    date_nasc = models.DateField()

    def __str__(self):
        return self.name


COURSE_LEVEL_CHOICES = (
    ("B", "Basic"),
    ("I", "Intermediate"),
    ("A", "Advanced"),
)


class Course(models.Model):
    description = models.TextField()
    code_course = models.CharField(max_length=10)
    nivel = models.CharField(
        max_length=1, choices=COURSE_LEVEL_CHOICES, blank=False, null=False, default="B"
    )

    def __str__(self):
        return self.description
