from rest_framework import viewsets, generics
from school.models import Student, Course, Matriculation
from school.serializers import (
    StudentSerializer,
    CourseSerializer,
    MatriculationSerializer,
    ListMatriculationStudentsSerializer,
    ListStudentsMatriculationACourseSerializer,
)
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class StudentsViewSet(viewsets.ModelViewSet):
    """Show all students"""

    queryset = Student.objects.all().order_by("id")  # Query all students
    serializer_class = StudentSerializer  # Serialize the data to JSON
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]


class CoursesViewSet(viewsets.ModelViewSet):
    """Show all courses"""

    queryset = Course.objects.all().order_by("id")
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]


class MatriculationsViewSet(viewsets.ModelViewSet):
    """Show all matriculations"""

    queryset = Matriculation.objects.all().order_by("id")
    serializer_class = MatriculationSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]


class ListMatriculationStudentsViewSet(generics.ListAPIView):
    """List matriculated from student"""

    serializer_class = ListMatriculationStudentsSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]

    def get_queryset(self):
        queryset = Matriculation.objects.filter(student_id=self.kwargs["pk"])
        return queryset


class ListStudentsMatriculationACourseViewSet(generics.ListAPIView):
    """List students matriculated in a course"""

    serializer_class = ListStudentsMatriculationACourseSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]

    def get_queryset(self):
        queryset = Matriculation.objects.filter(course_id=self.kwargs["pk"])
        return queryset
