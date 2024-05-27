from django.test import SimpleTestCase
from django.contrib.admin.sites import AdminSite
from school.admin import StudentAdmin
from school.models import Student


class StudentAdminTest(SimpleTestCase):
    def setUp(self) -> None:
        self.site = AdminSite()
        self.model_admin_student = StudentAdmin(Student, self.site)

    def test_model_admin_andamento_string_representation(self):
        assert str(self.model_admin_student) == "school.StudentAdmin"

    def test_quantity_actions_model_admin_andamento_should_return_2(self):
        actions_model = self.model_admin_student.actions
        quantity_actions = 0

        assert len(actions_model) == quantity_actions

    def test_list_display_should_return_correct_list(self):
        expected_fields = (
            "id",
            "name",
            "rg",
            "cpf",
            "date_nasc",
        )

        assert self.model_admin_student.list_display == expected_fields

    def test_list_display_links_should_return_correct_list(self):
        expected_fields = ("id", "name")

        assert self.model_admin_student.list_display_links == expected_fields

    def test_list_per_page_should_return_20(self):
        expected_quantity_page = 20
        assert self.model_admin_student.list_per_page == expected_quantity_page

    def test_list_filter_should_return_correct_list(self):
        expected_fields = (
            "name",
            "cpf",
        )

        assert self.model_admin_student.list_filter == expected_fields

    def test_search_fields_should_return_correct_list(self):
        expected_fields = ("name",)

        assert self.model_admin_student.search_fields == expected_fields
