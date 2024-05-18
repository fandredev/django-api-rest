from django.contrib import admin
from django.urls import path, include

from school.views import StudentsViewSet, CoursesViewSet, MatriculationsViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register("students", StudentsViewSet, basename="students")
router.register("courses", CoursesViewSet, basename="courses")
router.register("matriculations", MatriculationsViewSet, basename="matriculations")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
