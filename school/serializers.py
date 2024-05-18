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


class ListMatriculationStudentsSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(
        source="course.description"
    )  # This field is read-only and course.description is the source of the data
    period = serializers.SerializerMethodField()  # Create a function to get the period

    class Meta:
        model = Matriculation
        fields = ["course", "period"]

    def get_period(self, obj):
        return obj.get_period_display()


class ListStudentsMatriculationACourseSerializer(serializers.ModelSerializer):
    aluno_name = serializers.ReadOnlyField(
        source="student.name"
    )  # Read a field from the student model

    class Meta:
        model = Matriculation
        fields = ["aluno_name"]
