import os
import django
import random
from faker import Faker

# Set settings first
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project1.settings")

# Setup Django
django.setup()

# Import models AFTER setup
from firstapp.models import Student


faker = Faker("en_IN")


def population(n):
    for i in range(n):
        fname = faker.name()
        age = random.randint(17, 25)
        address = faker.address()
        rank = random.randint(1, 5000)
        college = faker.company() + " College"
        phone = faker.phone_number()

        Student.objects.create(
            ename=fname,
            eage=age,
            eadd=address,
            erank=rank,
            ecollege=college,
            ephno=phone
        )

    print(f"{n} records inserted successfully ✅")


population(10)
