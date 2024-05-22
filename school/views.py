from rest_framework import viewsets, generics, filters
from school.models import Student, Course, Matriculation
from school.serializers import (
    StudentSerializer,
    StudentSerializerV2,
    CourseSerializer,
    MatriculationSerializer,
    ListMatriculationStudentsSerializer,
    ListStudentsMatriculationACourseSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from http import HTTPStatus
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class StudentsViewSet(viewsets.ModelViewSet):
    """Show all students"""

    queryset = Student.objects.all().order_by("id")  # Query all students
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    ordering_fields = ["id"]
    search_fields = ["name", "cpf"]

    def get_serializer_class(self):
        if self.request.version == "v2":  # type: ignore
            return StudentSerializerV2
        return StudentSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    """Show all courses"""

    queryset = Course.objects.all().order_by("id")
    serializer_class = CourseSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    ordering_fields = ["id"]
    search_fields = ["nivel", "code_course"]

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=HTTPStatus.CREATED)
            id = str(serializer.data["id"])  # type: ignore
            response["Location"] = f"request.build_absolute_uri/{id}"

            return response


class MatriculationsViewSet(viewsets.ModelViewSet):
    """Show all matriculations"""

    queryset = Matriculation.objects.all().order_by("id")
    serializer_class = MatriculationSerializer
    http_method_names = ["get", "head", "post", "put", "patch", "delete"]

    @method_decorator(cache_page(15))
    def dispatch(self, *args, **kwargs):
        return super(MatriculationsViewSet, self).dispatch(*args, **kwargs)


class ListMatriculationStudentsViewSet(generics.ListAPIView):
    """List matriculated from student"""

    serializer_class = ListMatriculationStudentsSerializer

    def get_queryset(self):
        queryset = Matriculation.objects.filter(student_id=self.kwargs["pk"])
        return queryset


class ListStudentsMatriculationACourseViewSet(generics.ListAPIView):
    """List students matriculated in a course"""

    serializer_class = ListStudentsMatriculationACourseSerializer

    def get_queryset(self):
        queryset = Matriculation.objects.filter(course_id=self.kwargs["pk"])
        return queryset
