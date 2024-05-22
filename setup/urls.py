from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from school.views import (
    StudentsViewSet,
    CoursesViewSet,
    MatriculationsViewSet,
    ListMatriculationStudentsViewSet,
    ListStudentsMatriculationACourseViewSet,
)
from rest_framework import routers

router = routers.DefaultRouter()

router.register("students", StudentsViewSet, basename="students")
router.register("courses", CoursesViewSet, basename="courses")
router.register("matriculations", MatriculationsViewSet, basename="matriculations")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path(
        "students/<int:pk>/matriculations/",
        ListMatriculationStudentsViewSet.as_view(),
        name="student_matriculations",
    ),
    path(
        "courses/<int:pk>/matriculations/",
        ListStudentsMatriculationACourseViewSet.as_view(),
        name="course_matriculations",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
