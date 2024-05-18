from rest_framework import serializers
from school.models import Student, Course, Matriculation


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "name", "rg", "cpf", "date_nasc"]


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "description", "code_course", "nivel"]


class MatriculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matriculation
        exclude = []
