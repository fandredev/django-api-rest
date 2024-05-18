from django.http import JsonResponse
from django.http import HttpRequest
from .models import Student


def students(request: HttpRequest):
    students = Student.objects.all()
    if request.method == "GET":
        return JsonResponse({"students": students})
