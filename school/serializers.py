from rest_framework import serializers
from school.models import Student, Course, Matriculation
import re
from validate_docbr import CPF


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "name", "rg", "cpf", "date_nasc", "photo"]

    # TODO: move to validators.py
    def validate_cpf(self, cpf: str):
        cpf_instance = CPF()
        if not cpf_instance.validate(cpf):
            raise serializers.ValidationError("O CPF informado é inválido.")
        return cpf

    def validate_rg(self, rg: str):
        """Validate the RG format using RE"""
        if not re.match(r"\d{2}\.\d{3}\.\d{3}-\d{1,2}", rg):
            raise serializers.ValidationError(
                "O RG deve ter o formato XX.XXX.XXX-X. Verifique as pontuações."
            )
        return rg

    def validate_name(self, name: str):
        if not name.isalpha():
            raise serializers.ValidationError("O nome deve conter apenas letras.")
        return name


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


# v2


class StudentSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "name", "rg", "cpf", "phone", "date_nasc", "photo"]
