import os, django
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
django.setup()

from faker import Faker
import random
from school.models import Course


def create_courses(quantity_courses: int):
    Faker.seed(10)
    for _ in range(quantity_courses):
        code_course = "{}{}-{}".format(
            random.choice("ABCDEF"), random.randrange(10, 99), random.randrange(1, 9)
        )
        descs = [
            "Python Fundamentos",
            "Python intermediário",
            "Python Avançado",
            "Python para Data Science",
            "Python/React",
        ]
        description = random.choice(descs)
        descs.remove(description)
        nivel = random.choice("BIA")
        c = Course(code_course=code_course, description=description, nivel=nivel)
        c.save()


create_courses(10)
print("Courses created successfully! Quantity: 10")
