from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    rg = models.CharField(max_length=15, unique=True)
    cpf = models.CharField(max_length=15, unique=True)
    date_nasc = models.DateField()
    phone = models.CharField(max_length=15, default="")
    photo = models.ImageField(blank=True)

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


PERIOD_CHOICES = (
    ("M", "Morning"),
    ("A", "Afternoon"),
    ("N", "Night"),
)


class Matriculation(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE
    )  # One matriculation has one student
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE
    )  # One matriculation has one course
    period = models.CharField(
        max_length=1, choices=PERIOD_CHOICES, blank=False, null=False, default="M"
    )

    def __str__(self):
        return f"{self.student} - {self.course}"
