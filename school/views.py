from rest_framework import viewsets
from school.models import Student, Course, Matriculation
from school.serializers import (
    StudentSerializer,
    CourseSerializer,
    MatriculationSerializer,
)


class StudentsViewSet(viewsets.ModelViewSet):
    """Show all students"""

    queryset = Student.objects.all().order_by("id")  # Query all students
    serializer_class = StudentSerializer  # Serialize the data to JSON


class CoursesViewSet(viewsets.ModelViewSet):
    """Show all courses"""

    queryset = Course.objects.all().order_by("id")  # Query all courses
    serializer_class = CourseSerializer  # Serialize the data to JSON


class MatriculationsViewSet(viewsets.ModelViewSet):
    """Show all matriculations"""

    queryset = Matriculation.objects.all().order_by("id")  # Query all matriculations
    serializer_class = MatriculationSerializer  # Serialize the data to JSON
