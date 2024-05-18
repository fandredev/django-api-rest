from rest_framework import serializers
from school.models import School, Course


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ["id", "name", "rg", "cpf", "date_nasc"]


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "description", "code_course"]
