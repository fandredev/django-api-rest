from rest_framework.test import APITestCase
from school.models import Course
from django.urls import reverse
from http import HTTPStatus
from django.contrib.auth.models import User
from faker import Faker


class CoursesTestCase(APITestCase):

    def setUp(self) -> None:
        self.faker = Faker("pt_BR")

        self.user = User.objects.create_superuser(
            username="admin", email=self.faker.email(), password="admin"
        )
        self.list_url = reverse("courses-list")
        self.course_one = Course.objects.create(
            code_course="CTT1", description="Course Test 1"
        )
        self.course_two = Course.objects.create(
            code_course="CTT2", description="Course Test 2", nivel="I"
        )

    def test_request_get_courses_should_return_status_401_when_user_not_authorizated(
        self,
    ):
        response = self.client.get(self.list_url)
        self.assertEqual(HTTPStatus.UNAUTHORIZED, response.status_code)

    def test_request_get_courses_should_return_status_200(self):
        self.client.force_authenticate(self.user)  # type: ignore
        response = self.client.get(self.list_url)
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_request_create_course_should_return_201(self):
        self.client.force_authenticate(self.user)  # type: ignore
        data = {"code_course": "CTT3", "description": "Course Test 3"}
        response = self.client.post(self.list_url, data=data, format="json")

        self.assertEqual(HTTPStatus.CREATED, response.status_code)
