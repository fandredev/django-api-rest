from django.contrib import admin

from school.models import Student, Course

# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "rg",
        "cpf",
        "date_nasc",
    )
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_filter = ("name", "cpf")
    list_per_page = 20


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "description",
        "code_course",
    )
    list_display_links = (
        "id",
        "code_course",
    )
    search_fields = ("code_course",)
    list_filter = ("description", "code_course")
    list_per_page = 20
