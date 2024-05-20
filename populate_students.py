import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from school.models import Student


def create_students(quantity_students: int):
    fake = Faker("pt_BR")
    Faker.seed(10)
    for _ in range(quantity_students):
        cpf = CPF()
        name = fake.name()
        cpf = cpf.generate()
        rg = "{}{}{}{}".format(
            random.randrange(10, 99),
            random.randrange(100, 999),
            random.randrange(100, 999),
            random.randrange(0, 9),
        )
        date_nasc = fake.date_of_birth()
        student = Student(name=name, cpf=cpf, rg=rg, date_nasc=date_nasc)
        student.save()


create_students(50)
print("Students created successfully! Quantity: 50")
