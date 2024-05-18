from django.contrib import admin
from django.urls import path, include

from school.views import students

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("students/", students),
]
